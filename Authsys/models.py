from django.db import models
from django.contrib.auth.models import User
from MainApp.models import Basket


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')  # user.userprofile
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    basket = models.OneToOneField(Basket, on_delete=models.SET_NULL, blank=True, null=True)  # basket.userprofile

    def __str__(self):
        return f"Userprofile for {self.user.username}"
