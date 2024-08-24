# tasks.py
from time import sleep

from tesserocr import PyTessBaseAPI
import os

from celery_app import celery  # Importer l'instance de Celery depuis app.py
from services.dispatch import dispactcher

@celery.task
def test_task_sleep():
    sleep(10)
    return "Task done"

@celery.task
def ocr_document(filename, file_path):
    text = dispactcher(filename, file_path)
    os.remove(file_path)
    return text