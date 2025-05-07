import json, pika
from dotenv import load_dotenv
from main import Product, db, app

# Load environment variables
load_dotenv()

params = pika.URLParameters("amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw")
connection = pika.BlockingConnection(params)
channel = connection.channel()
# creates the 'main' queue (if it doesn't exist)
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    try:
        print('Received in main')
        data = json.loads(body)
        print(data)

        with app.app_context():
            if properties.content_type == 'product_created':
                product = Product(id=data['id'], title=data['title'], image=data['image'])
                db.session.add(product)
                db.session.commit()
                print('Product Created')

            elif properties.content_type == 'product_updated':
                product = Product.query.get(data['id'])
                product.title = data['title']
                product.image = data['image']
                db.session.commit()
                print('Product Updated')


            elif properties.content_type == 'product_updated_partial':
                product = Product.query.get(data['id'])
                if data.get('title'):
                    product.title = data['title']
                if data.get('image'):
                    product.image = data['image']
                db.session.commit()
                print('Product Updated Partial')


            elif properties.content_type == 'product_deleted':
                product = Product.query.get(data)
                db.session.delete(product)
                db.session.commit()
                print('Product Deleted')
    except Exception as e:
        print(f"Error processing message: {e}")

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)  # Consumes messages from 'main'
print('Started Consuming')

try:
    channel.start_consuming()
finally:
    channel.close()
    connection.close()