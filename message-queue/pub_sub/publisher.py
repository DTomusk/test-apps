import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# All messages go to an exchange (not directly to the queue)
# An exchange has a type
# The default exchange '' sends messages to the queue with the routing_key (if it exists)
# 'fanout' sends it to all queues
channel.exchange_declare(exchange='pub',
                         exchange_type='fanout')

# We don't need to declare a queue here anymore

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
# As opposed to before, we're not using a routing_key as messages go to all queues
# Messages will be lost if no queue is bound to the exchange
channel.basic_publish(exchange='pub',
                      routing_key='',
                      body=message)

print(f" [x] Sent {message}")

connection.close()