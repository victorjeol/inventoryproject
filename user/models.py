from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    profile_image = models.ImageField(default='avatar.jpg', upload_to='profile_images')


    def __str__(self):
        return f'{self.staff.username}-Profile'
