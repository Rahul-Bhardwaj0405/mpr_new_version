from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'folder_upload_app.settings')
app = Celery('folder_upload_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
