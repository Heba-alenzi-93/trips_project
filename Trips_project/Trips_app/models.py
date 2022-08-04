from distutils.command.upload import upload
from sys import maxsize
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Trip (models.Model):
    title = models.CharField(max_length=100)
    #description = models.TextField ( maxsize = 1000)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="avtars/",null=True )
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to="avtars/",null=True ,blank=True)


    def __str__(self):
        return self.user