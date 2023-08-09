import os

from dotenv import load_dotenv

load_dotenv()

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
CELERY_TASK_SERIALIZER = os.getenv("CELERY_TASK_SERIALIZER", "json")

if not any([CELERY_BROKER_URL, CELERY_RESULT_BACKEND]):
    raise Exception("Missing Celery broker / backend")

broker_url = CELERY_BROKER_URL
result_backend = CELERY_RESULT_BACKEND

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'America/Sao_Paulo'
enable_utc = True
