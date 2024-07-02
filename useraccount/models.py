from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    profile = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.first_name