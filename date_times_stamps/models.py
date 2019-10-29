from django.db import models

# Create your models here.


class DateTimeStamps(models.Model):
    date_time = models.DateTimeField()
    time_in = models.CharField(max_length=3)