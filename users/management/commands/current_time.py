from django.core.management.base import BaseCommand
import datetime
from app.settings import TIME_ZONE


class Command(BaseCommand):
    help = 'Displays current times UTC & PST'

    def handle(self, *args, **options):
        print('Time in UTC::', datetime.datetime.utcnow())
        print('Time in PST::', datetime.datetime.now())







