from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, null=False)
    password = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=2, null=False)
    gender = models.CharField(max_length=1, null=False)
    dob = models.DateField(null=False)
