import pika

params = pika.URLParameters("amqps://yrhxzdbw:8Y9GmUDjgzTe6LEUCDuhx_516VWOrYRd@rattlesnake.rmq.cloudamqp.com/yrhxzdbw")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')  # Declares the 'admin' queue (ensures it exists)

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)  # Consumes messages from 'admin'

print('Started Consuming')

channel.start_consuming()  # Keeps the consumer running

channel.close()  # Closes the connection
