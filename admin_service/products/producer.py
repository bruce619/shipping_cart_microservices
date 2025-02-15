#amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw

import pika

params = pika.URLParameters('amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw')  # Connects to RabbitMQ server

connection = pika.BlockingConnection(params)  # Creates a connection
channel = connection.channel()  # Opens a channel to communicate with RabbitMQ


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')  # Publishes a message to the queue named 'admin'







