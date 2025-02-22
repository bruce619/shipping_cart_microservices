import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

# Load environment variables
load_dotenv()

username = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')

print("username:", username, " password:", password)

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{username}:{password}@db:5432/main"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    __tablename__ = 'product_user'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/')
def index():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')