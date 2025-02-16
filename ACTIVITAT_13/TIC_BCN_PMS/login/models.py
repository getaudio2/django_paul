from django.db import models

# Create your models here.
class User(models.Model):
    nom = models.CharField(max_length=30)
    cognom = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)