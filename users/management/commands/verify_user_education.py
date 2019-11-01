from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):

    help = "Verify User Education"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, nargs='?', help='Define a user id')
        parser.add_argument('-a', '--all', type=bool, nargs='?', default=False, help="Get all users education status")

    def handle(self, *args, **options):
        id = options['id'] or ''
        url = 'http://localhost:8000/users/{0}'.format(id)
        response = requests.get(url=url)
        response = response.json()
        print(response)