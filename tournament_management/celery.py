
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery  # Ensure there is no local file named 'celery.py'

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tournament_management.settings')

# Create an instance of the Celery application.
app = Celery('tournament_management')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
