from django.db import models


# Create your models here.
class Product(models.Model):
    PpName = models.CharField(max_length=20)
    Pprice = models.IntegerField()
    Pcolor = models.CharField(max_length=20)
    Quantity = models.IntegerField()
