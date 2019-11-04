from django.core.management.base import BaseCommand
import requests
from django.contrib.auth import get_user_model
from users.models import EducationInformation
from django.core.exceptions import ObjectDoesNotExist
from users.serializers import UserEducationInformationSerializer
User = get_user_model()

class Command(BaseCommand):

    help = "Verify User Education"


    def add_arguments(self, parser):
        parser.add_argument('id', type=int, nargs='?', help='Define a user id')
        parser.add_argument('-a', '--all', type=bool, nargs='?', default=False, help="Get all users education status")

    def handle(self, *args, **options):
        is_all = options['all']
        user_id = options['id']
        degree_ids = list()
        if is_all:
            users = User.objects.prefetch_related('educations')
            for user in users:
                user_education_info = user.educations.order_by('-degree_completed_date').first()
                if user_education_info:
                    context = UserEducationInformationSerializer(user_education_info).data
                    response = self.verify_degree_api(user.username, **context).json()

                    if len(response):
                        degree_ids.append(user_education_info.id)

        elif user_id:
            try:
                user = User.objects.prefetch_related('educations').get(id=user_id)
                user_education_info = user.educations.order_by('-degree_completed_date').first()
                if user_education_info:
                    context = UserEducationInformationSerializer(user_education_info).data
                    response = self.verify_degree_api(user.username, **context).json()
                    if len(response):
                        degree_ids.append(user_education_info.id)
            except ObjectDoesNotExist as e:
                self.stdout.write("Invalid id, please enter valid user id.")

        if len(degree_ids):
            EducationInformation.objects.filter(pk__in=degree_ids).update(is_verified =True)

    def verify_degree_api(self, username, **options):
        params = dict()
        url = 'http://localhost:8000/verify-degree/'
        params['username'] = username
        params['degree_name'] = options['degree_name']
        params['cgpa'] = options['cgpa']
        return requests.get(url=url,params=params)