#amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw
import pika

params = pika.URLParameters('amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw')

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