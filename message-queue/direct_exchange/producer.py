# Direct exchange is different to fanout 
# Where fanout broadcasts a message to all queues, 
# direct exchange sends messages to queues with the matching routing key (binding key)
# this allows you to control exactly where your messages go 
# a queue can have multiple bindings to an exchange, so it can receive multiple "types" of message
# importantly, if there are no bindings for a given routing key, those message will simply be discarded

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange_type='direct', exchange='foo')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='foo', routing_key=severity, body=message)

print(f" [x] Sent {severity}:{message}")

connection.close()