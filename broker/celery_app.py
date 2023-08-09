from celery import Celery

from celeryconfig import CELERY_BROKER_URL


celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_BROKER_URL)
celery_app.autodiscover_tasks()
