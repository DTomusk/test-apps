import pika


def create_and_run_sub(callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # This needs to be in both pub and sub
    channel.exchange_declare(exchange='pub', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # the relationship between an exchange and a queue is a binding
    # the binding tells the exchange to send messages to this queue
    channel.queue_bind(exchange="pub", queue=queue_name)

    # Make sure the consume is set up on the correct queue 
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()