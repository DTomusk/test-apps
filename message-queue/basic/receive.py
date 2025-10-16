import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # call is idempotent, make sure to call to ensure the queue exists 
    channel.queue_declare(queue='hello')

    # function to call when message received, can access properties of message (incl. body)
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # auto_ack acknowledges receiving a message when it gets it, so if the worker fails to process a message
    # after receiving it, the message will never get processed 
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

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