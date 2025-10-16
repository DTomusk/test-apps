from create_sub import create_and_run_sub

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

create_and_run_sub(callback)