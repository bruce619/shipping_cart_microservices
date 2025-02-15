import os
import pika

CLOUDAMQP_URL = os.getenv('CLOUDAMQP_URL')
params = pika.URLParameters(CLOUDAMQP_URL)  # Connects to RabbitMQ server

connection = pika.BlockingConnection(params)  # Creates a connection
channel = connection.channel()  # Opens a channel to communicate with RabbitMQ


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')  # Publishes a message to the queue named 'admin'







