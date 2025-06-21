from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    Pname = models.CharField(max_length=20)
    Pprice = models.IntegerField()
    Pcolor = models.CharField(max_length=20)
    Quantity = models.IntegerField()

    # List view redirect
    # def get_absolute_url(self):
    #     return reverse('pro1')

    # Detail view redirect
    def get_absolute_url(self):
        return reverse('pro2', args={self.pk})
