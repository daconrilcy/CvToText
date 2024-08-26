# tasks.py
from time import sleep
import os

from celery_app import celery  # Importer l'instance de Celery depuis celery_app.py
from services.dispatch import dispatcher  # Correction de l'import du dispatcher


@celery.task
def test_task_sleep(time=10):
    sleep(time)
    return "Task done in {} seconds".format(time)


@celery.task
def ocr_document(filename, file_path):
    text = dispatcher(filename, file_path)  # Correction de la fonction dispatcher
    os.remove(file_path)
    return text