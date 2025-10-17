import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Topic exchange allows for structured routing keys which are . delimited 
channel.exchange_declare(exchange='topic_exchange', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'foo.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='topic_exchange', routing_key=routing_key, body=message)

print(f" [x] Sent {routing_key}:{message}")

connection.close()