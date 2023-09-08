from django.db import models

# Create your models here.


class Stack(models.Model):
  slack_name = models.CharField(max_length=200)
  current_day = models.DateField()
  utc_time = models.DateTimeField()
  track = models.CharField(max_length=200)
  