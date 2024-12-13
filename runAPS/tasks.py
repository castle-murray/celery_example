from celery import shared_task

@shared_task
def print_time():
    print("bacon")
