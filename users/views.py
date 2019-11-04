
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer, UserEducationInformationSerializer, DegreeSerializer
from .models import EducationInformation, Degree
# Create your views here.

User = get_user_model()
# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserEducationInfoViewSet(viewsets.ModelViewSet):
    queryset = EducationInformation.objects.all()
    serializer_class = UserEducationInformationSerializer


class DegreeVerifyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_params = self.request.query_params
        if query_params:
            queryset = Degree.objects.filter(username=query_params.get('username'),degree_name=query_params.get('degree_name'),cgpa=query_params.get('cgpa'))
        return queryset
