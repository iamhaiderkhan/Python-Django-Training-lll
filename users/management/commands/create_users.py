from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):

    help = "Create multiple users"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

        parser.add_argument('-p', '--prefix', type=str, help="Define a username prefix.")
        parser.add_argument('-b', '--bulk', type=bool, nargs='?', default=False, help="Bulk create key.")

    def handle(self, *args, **options):
        total = options['total']
        prefix = options['prefix']
        is_bulk = options['bulk']

        users_list = list()

        for i in range(total):
            if prefix:
                if is_bulk is True:
                    username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
                    users_list.append(User(username=username, email='', password= make_password('123')))
                else:
                    username = '{prefix}_{random_string}'.format(prefix=prefix, random_string=get_random_string())
                    User.objects.create_user(username= username, email='', password='123')
            else:
                if is_bulk is True:
                    username = get_random_string()
                    users_list.append(User(username=username, email='', password=make_password('123')))
                else:
                    username = get_random_string()
                    User.objects.create_user(username= username, email='', password='123')

        if is_bulk is True:
            print(users_list)
            User.objects.bulk_create(users_list)