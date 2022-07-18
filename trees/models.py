from django.db import models

from accounts.models import Account
from trees.managers import PlantedTreesManager
from users.models import User


class Tree(models.Model):
    name = models.CharField(max_length=80)
    scientific_name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.scientific_name


class PlantedTree(models.Model):
    age = models.IntegerField(default=0)
    planted_at = models.DateTimeField("date tree was planted", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    objects = PlantedTreesManager()

    def __str__(self):
        return self.tree
