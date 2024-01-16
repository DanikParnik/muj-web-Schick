from django.db import models

# Create your models here.
class model1(models.Model):
    nahodnepolicko=models.CharField
    autor = models.CharField(max_length=200, default="x")
    nazev = models.CharField(max_length=200, default="x")
    prispevek = models.CharField(max_length=200, default="x")
