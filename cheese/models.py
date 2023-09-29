from django.db import models

# Create your models here.
class cheese(models.Model):
    name=models.CharField(max_length=200)
    origin=models.CharField(max_length=200)
    type=models.CharField(max_length=200)