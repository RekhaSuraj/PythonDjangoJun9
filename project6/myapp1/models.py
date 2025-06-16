from django.db import models


# Create your models here.
class Car(models.Model):
    Name = models.CharField(max_length=30)
    Color = models.CharField(max_length=20)
    Price = models.IntegerField()
    Launch = models.DateField()
