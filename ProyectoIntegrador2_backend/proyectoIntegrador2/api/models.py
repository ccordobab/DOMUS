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

class Place(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    STATE_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    employee = models.ManyToManyField(Employee)
    name = models.CharField(max_length=50)
    place = models.ManyToManyField(Place)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='scheduled')
    time = models.DateTimeField()

class Tarea(models.Model):
    STATE_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='scheduled')
    time = models.CharField(max_length=50)

class Excusa(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    fromDate = models.CharField(max_length=50)
    toDate = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

class Maintenance(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    maintenanceType = models.CharField(max_length=50)
    completed = models.BooleanField