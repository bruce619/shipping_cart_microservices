import os
import pika

CLOUDAMQP_URL = os.getenv('CLOUDAMQP_URL')
params = pika.URLParameters(CLOUDAMQP_URL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')  # Declares the 'main' queue (ensures it exists)

def callback(ch, method, properties, body):
    print('Received in main')
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback)  # Consumes messages from 'main'

print('Started Consuming')

channel.start_consuming()  # Keeps the consumer running

channel.close()  # Closes the connection

# checking