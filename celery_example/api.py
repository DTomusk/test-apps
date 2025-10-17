from fastapi import FastAPI
from celery_example.worker import celery_app, add

app = FastAPI()

@app.post("/")
def queue_tasks_and_do_stuff():
    task = add.delay(4, 4)
    return {"message" : "API call done"}