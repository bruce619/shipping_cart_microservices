import os, django, pika, json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Force environment variables
os.environ['POSTGRES_HOST'] = 'db'
os.environ['POSTGRES_PORT'] = '5432'


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_service.settings')
django.setup()

from products.models import Product

# Connects to RabbitMQ server (CloudAMQP)
params = pika.URLParameters("amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw")
connection = pika.BlockingConnection(params)
channel = connection.channel()
# creates the 'admin' queue (if it doesn't exist)
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    try:
        print('Received in admin')
        id = json.loads(body)
        print(id)
        product = Product.objects.get(id=id)
        product.likes = product.likes + 1
        product.save()
        print('product likes increased')
    except Exception as e:
        print(f"Error processing message: {e}")

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)  # Consumes messages from 'admin'
print('Started Consuming')

try:
    channel.start_consuming()
finally:
    channel.close()
    connection.close()