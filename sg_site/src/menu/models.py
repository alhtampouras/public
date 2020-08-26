from django.db import models
from pathlib import Path
from multiselectfield import MultiSelectField as MSF

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ingredients = ((1,'Τομάτα'),(2,'Iceberg'),(3,'Πίκλες'))

# Create your models here.
class Burgers(models.Model):
    name        = models.CharField(max_length = 80,blank=False)
    ingredients = MSF(choices=ingredients, blank=False)
    price       = models.FloatField(blank=False)
    photo       = models.ImageField(upload_to=BASE_DIR / '/static/pics', blank=True)
