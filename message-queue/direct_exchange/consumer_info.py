import pika

from models import severity

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange_type='direct', exchange='foo')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# binds just the info severity, probably not very practical, but good for practice
channel.queue_bind(exchange='foo',
                    queue=queue_name,
                    routing_key=severity.info.name)
    
print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()