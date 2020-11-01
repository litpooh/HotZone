from django.db import models

# Create your models here.
class Location(models.Model):
    nameZH = models.CharField(max_length=500)
    nameEN = models.CharField(max_length=200)
    addressZH = models.CharField(max_length=500)
    addressEN = models.CharField(max_length=500)
    x = models.DecimalField(max_digits=20, decimal_places=0)
    y = models.DecimalField(max_digits=20, decimal_places=0)
    def __str__(self):
        return self.nameEN

class SearchResult(models.Model):
    nameZH = models.CharField(max_length=500)
    nameEN = models.CharField(max_length=200)
    addressZH = models.CharField(max_length=500)
    addressEN = models.CharField(max_length=500)
    x = models.DecimalField(max_digits=20, decimal_places=0)
    y = models.DecimalField(max_digits=20, decimal_places=0)
    def __str__(self):
        return self.nameEN
