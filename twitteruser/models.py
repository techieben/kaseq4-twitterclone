from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone


class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username
