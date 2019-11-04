from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.


class CustomUser(AbstractUser):
    pass


class EducationInformation(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='educations', verbose_name='education', on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    degree_started_date = models.DateField()
    degree_completed_date = models.DateField()
    cgpa = models.FloatField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.degree_name


class Degree(models.Model):
    username = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    cgpa = models.FloatField()

    def __str__(self):
        return self.degree_name





