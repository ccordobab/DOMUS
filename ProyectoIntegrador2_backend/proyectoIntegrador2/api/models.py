from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)