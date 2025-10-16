import time
import pika, sys, os

# If you run multiple workers, rabbitmq will use round-robin to distribute messages
# The nth worker will get the nth message etc.
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # call is idempotent, make sure to call to ensure the queue exists 
    channel.queue_declare(queue='tasks', durable=True)

    # Callback that sleeps for every '.' in the message it receives     
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        # Sends an acknowledgement once the task is done processing 
        # If rabbit doesn't receive this, then it requeues the task to another worker 
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # Ensures that a worker doesn't have more than one task at a time 
    # Note: this may cause the queue to fill up
    channel.basic_qos(prefetch_count=1)

    # Important! With auto_ack removed, you need to ensure the callback has an ack on it e.g. ch.basic_ack
    # Otherwise rabbit will think messages haven't been received and requeue them for other workers
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    # quit on ctrl+c
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)