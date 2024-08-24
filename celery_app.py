# celery_app.py
from celery import Celery

def make_celery():
    celery_obj = Celery('tasks', include=['tasks'])
    celery_obj.conf.broker_url = 'redis://localhost:6379/0'
    celery_obj.conf.result_backend = 'redis://localhost:6379/1'
    celery_obj.conf.broker_connection_retry_on_startup = True
    celery_obj.autodiscover_tasks()
    return celery_obj

celery = make_celery()