from django.db import models


class Sensors(models.Model):
    pressure = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    depth = models.CharField(max_length=50)
