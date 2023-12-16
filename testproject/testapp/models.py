from django.db import models
from datetime import date

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(default=date(2023, 12, 28))
    price = models.FloatField()
    duration = models.IntegerField()
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    min_age = models.IntegerField()
    destination = models.CharField(max_length=50)

class Guide(models.Model):
    name = models.CharField(max_length=50, default="Miguel")
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    experience = models.IntegerField()
    sp_english = models.BooleanField()
    sp_georgian = models.BooleanField()
    sp_spanish = models.BooleanField()
    sp_japanese = models.BooleanField()
    image = models.CharField(max_length=50)
    tours = models.ManyToManyField(Tour)

