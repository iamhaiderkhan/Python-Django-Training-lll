from django.core.management.base import BaseCommand
import requests
from django.contrib.auth import get_user_model
from users.models import EducationInformation
from django.core.exceptions import ObjectDoesNotExist
from users.serializers import UserEducationInformationSerializer
from urllib.parse import urlencode
User = get_user_model()


class Command(BaseCommand):

    help = "Verify User Education"
    degree_ids = list()

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, nargs='?', help='Define a user id')
        parser.add_argument('-a', '--all', type=bool, nargs='?', default=False, help="Get all users education status")

    def handle(self, *args, **options):
        is_all = options['all']
        user_id = options['id']

        if is_all:
            users = User.objects.prefetch_related('educations')
            self.stdout.write("Total Number of Users: {0}".format(len(users)))
            for index, user in enumerate(users, start=1):
                self.verify_user_education_info(user, index)
        elif user_id:
            try:
                user = User.objects.prefetch_related('educations').get(id=user_id)
                self.verify_user_education_info(user)
            except ObjectDoesNotExist as e:
                self.stdout.write("Invalid id, please enter valid user id.")
        if len(self.degree_ids):
            EducationInformation.objects.filter(pk__in=self.degree_ids).update(is_verified =True)

    def verify_user_education_info(self, user, index=1):
        user_education_info = user.educations.order_by('-degree_completed_date').first()
        if user_education_info:
            context = UserEducationInformationSerializer(user_education_info).data
            response = self.verify_degree_api(user.username, **context).json()
            self.stdout.write("{0}: Username:{1}, Education Status:{2}".format(index, user.username, "verified" if len(response) else "un-verified"))
            if len(response):
                self.degree_ids.append(user_education_info.id)
        else:
            self.stdout.write(
                "{0}: Username:{1}, Education Status:{2}".format(index, user.username,"un-verified"))

    def verify_degree_api(self, username, **options):
        params = dict()
        url = 'http://localhost:8000/verify-degree/'
        params['username'] = username
        params['degree_name'] = options['degree_name']
        params['cgpa'] = options['cgpa']
        return requests.get(url=url, params=urlencode(params))
