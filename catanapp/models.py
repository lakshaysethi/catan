from django.db import models

# Create your models here.

class Dropable(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to = 'dropables')
