import pika

from models import severity

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# bind each severity as a routing key so this consumer can consume any severity message
for sev in severity:
    channel.queue_bind(exchange='foo',
                       queue=queue_name,
                       routing_key=sev.name)
    
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()