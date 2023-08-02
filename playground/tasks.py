from time import sleep
from celery import shared_task

@shared_task
def notify_customers(message):
    print('Sending 10k message')
    print(message)
    sleep(10)
    print('Email were successfully sent!')