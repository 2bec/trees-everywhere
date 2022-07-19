from django.db import models

from django.contrib.auth.models import AbstractUser

from trees.models import PlantedTree


class User(AbstractUser):
    def plant_tree(self, tree, location):
        latitude, longitude = location
        PlantedTree.objects.create(
            user_id=self.id,
            tree_id=tree.id,
            latitude=latitude,
            longitude=longitude,
            account_id=self.accounts.first().id,
        )

    def plant_trees(self, plants):
        for plant in plants:
            tree, location = plant
            self.plant_tree(tree, location)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField()
    joined_at = models.DateTimeField("date user was joined to platform")
