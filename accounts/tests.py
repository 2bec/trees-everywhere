from django.test import TestCase, Client
from django.urls import reverse

from trees.models import PlantedTree
from users.models import User
from trees_everywhere.middleware import set_current_accounts, set_current_user


class AccountTestClass(TestCase):

    fixtures = ["users", "accounts", "trees", "planted_trees"]

    @classmethod
    def setUpTestData(cls):
        # create two accounts
        # create three users
        # create some trees
        # create some planted trees
        ...

    def test_user_can_plant_tree(self):
        ...

    def test_user_can_plant_trees(self):
        ...
