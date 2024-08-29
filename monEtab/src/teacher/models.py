from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    city = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    vacation = models.BooleanField()
    subject_taught = models.CharField(max_length=30)
    next_course = models.CharField(max_length=30)
    subject_next_meet = models.CharField(max_length=30)