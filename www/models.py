from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    image = models.CharField(max_length = 200)
