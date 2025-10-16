import sys, pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='tasks', durable=True)

# Read message from commandline or do Hello World! if absent
message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',
                      routing_key='tasks',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = pika.DeliveryMode.Persistent
                      ))
print(f" [x] Sent {message}")

connection.close()