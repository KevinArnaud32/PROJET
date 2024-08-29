from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=302)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    city = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    class_student = models.CharField(max_length=30)
    register_number = models.CharField(max_length=30)