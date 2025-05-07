import pika, json

# Connects to RabbitMQ server (CloudAMQP)
params = pika.URLParameters("amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw")
connection = pika.BlockingConnection(params)  # Creates a connection
channel = connection.channel()  # Opens a channel to communicate with RabbitMQ


def publish(method, body):
    properties = pika.BasicProperties(method)  # Creates a property object that labels the message
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)  # Publishes a message to the queue named 'admin'







