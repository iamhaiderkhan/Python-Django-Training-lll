from django.core.management.base import BaseCommand
import datetime
from app.settings import PST, UTC
from date_times_stamps.models import DateTimeStamps


class Command(BaseCommand):
    help = 'Displays current times UTC & PST'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of datetime stamps to be created')

    def handle(self, *args, **options):
        total = options['total']
        date_times_list = list()

        for i in range(total):
            date_times_list.append(DateTimeStamps(date_time=datetime.datetime.utcnow(), time_in=UTC))

        DateTimeStamps.objects.bulk_create(date_times_list)





