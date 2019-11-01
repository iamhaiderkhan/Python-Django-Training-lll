
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer, UserEducationInformationSerializer
from .models import EducationInformation
# Create your views here.

User = get_user_model()
# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserEducationInfoViewSet(viewsets.ModelViewSet):
    queryset = EducationInformation.objects.all()
    serializer_class = UserEducationInformationSerializer
