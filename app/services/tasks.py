from celery import shared_task
from django.core.management import call_command


@shared_task()
def dbackup_task():
    """
    Выполнение резервного копирования базы данных
    """
    call_command('dbackup')
