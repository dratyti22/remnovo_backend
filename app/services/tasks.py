from datetime import datetime, timedelta

from celery import shared_task
from django.core.management import call_command
import os


@shared_task()
def dbackup_task():
    """
    Выполнение резервного копирования базы данных
    """
    call_command('dbackup')


@shared_task()
def cleanup_backups():
    """
    Удаление бэкапов которым больше 1 месяца
    """
    backup_dir = 'backups'
    for file in os.listdir(backup_dir):
        file_path = os.path.join(backup_dir, file)
        if os.path.isfile(file_path):
            file_ctime = os.path.getctime(file_path)
            one_month_ago = (datetime.now() - timedelta(days=30)).timestamp()
            if file_ctime < one_month_ago:
                os.remove(file_path)
