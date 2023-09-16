from django.db import models

# Create your models here.

class Stack(models.Model):
  name = models.CharField(max_length=200,unique=True)