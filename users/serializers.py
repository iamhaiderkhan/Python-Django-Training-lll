from django.conf.urls import url, include
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import EducationInformation, Degree
from django.forms import model_to_dict
# Serializers define the API representation.

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()
    educations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'is_staff','full_name', 'educations')
        read_only_fields = ('is_active', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def get_full_name(self, obj):
        if obj.first_name and obj.last_name:
            return '{} {}'.format(obj.first_name, obj.last_name)
        return ""

    def get_educations(self, obj):

        try:
            education = EducationInformation.objects.filter(user=obj).order_by('-degree_completed_date').first()
            return model_to_dict(education)
        except AttributeError as e:
            education = dict()
            return education


class UserEducationInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EducationInformation
        fields = ('user', 'institute_name', 'degree_name', 'cgpa', 'degree_started_date', 'degree_completed_date', 'is_verified')


    def create(self, validated_data):
        educationinfo = super(UserEducationInformationSerializer, self).create(validated_data)
        Degree.objects.create(username=educationinfo.user.username, degree_name=educationinfo.degree_name, cgpa=educationinfo.cgpa)
        return educationinfo


class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = ('username', 'degree_name', 'cgpa')