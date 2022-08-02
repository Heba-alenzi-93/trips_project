from distutils.command.upload import upload
from sys import maxsize
from django.db import models

# Create your models here.


class Trip (models.Model):
    title = models.CharField(max_length=100)
    #description = models.TextField ( maxsize = 1000)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="avtars/",null=True )

    def __str__(self):
        return self.title