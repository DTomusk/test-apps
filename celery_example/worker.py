from celery import Celery

# Run with: 
# celery -A worker.celery_app worker --loglevel=info --pool=solo
celery_app = Celery(
    "celery_example",
    broker="amqp://guest@localhost//"
)

@celery_app.task(name="celery_example.worker.add")
def add(x, y):
    print("Celery thing got called!")
    return x + y