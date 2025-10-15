import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# creates or checks a queue
channel.queue_declare(queue='hello')

# publishes a message to the queue with the routing key
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

# flush and make sure message was sent before exiting
connection.close()