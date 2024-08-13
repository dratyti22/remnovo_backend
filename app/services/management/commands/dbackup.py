import os

from django.core.management import BaseCommand, call_command
from datetime import datetime


class Command(BaseCommand):
    """
    Команда для создания резервной копии базы данных
    """

    def handle(self, *args, **options):
        backup_dir = 'backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        call_command(
            'dumpdata',
            '--natural-foreign',
            '--natural-primary',
            '--exclude=contenttypes',
            '--exclude=admin.logentry',
            '--indent=4',
            f'--output={backup_dir}/database-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.json'
        )
