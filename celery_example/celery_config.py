from datetime import timedelta

# For scheduled tasks, you need to run a separate task scheduler to the worker 
# This is where you define the schedules for tasks 
# The scheduler calls a task at an interval the same way you'd call a celery task from another part of the system
beat_schedule = {
    'print-time-every-10-seconds': {
        'task': 'celery_example.worker.print_time',
        'schedule': timedelta(seconds=10),
    },
}

timezone = 'UTC'
