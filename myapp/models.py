from django.db import models

# Create your models here.
class Lecture(models.Model):
    classNo = models.CharField(max_length=10)
    className = models.CharField(max_length=30)
    professor = models.CharField(max_length=10)
    classRoomNo = models.CharField(max_length=10)