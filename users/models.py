from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def plant_tree():
        ...

    def plant_trees():
        ...


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField()
    joined_at = models.DateTimeField("date user was joined to platform")
