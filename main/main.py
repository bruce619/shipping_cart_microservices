import os
from dataclasses import dataclass
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint, exc
from producer import publish

# Load environment variables
load_dotenv()

username = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@db:5432/main"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app, origins=["http://localhost:3000", "http://localhost:8000", "http://host.docker.internal:8000"])

@dataclass
class Product(db.Model):
    __tablename__ = 'products'
    id: int
    title: str
    image: str
    likes: int
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    likes = db.Column(db.Integer)

@dataclass
class ProductUser(db.Model):
    __tablename__ = 'product_user'

    __table_args__ = (UniqueConstraint('user_id', 'product_id', name='user_product_unique'),)

    id: int
    product_id: int
    user_id: int
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

@app.route('/api/v1/products', methods=['GET'])
def index():
    return jsonify(Product.query.all())


@app.route('/api/v1/products/<int:id>/like', methods=['POST'])
def like(id):
    try:
        response = requests.get('http://host.docker.internal:8000/api/v1/users')
        response_json = response.json()
    except ValueError as e:
        return jsonify({"error": f"Invalid JSON response: {e}"}), 500

    try:
        product_user = ProductUser(product_id=id, user_id=response_json['id'])
        db.session.add(product_user)

        # Increment the like count in the Product table
        product = Product.query.get(id)
        if product is None:
            db.session.rollback()
            return jsonify({"error": "Product not found"}), 404

        product.likes = product.likes + 1 if product.likes else 1

        db.session.commit()

        # Publish to RabbitMQ
        publish('product_liked', id)

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({"error": "You already liked this product"}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred: {e}"}), 500

    return  jsonify({
        'message': 'Success',
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')