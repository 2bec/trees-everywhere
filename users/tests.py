from decimal import Decimal, getcontext
from django.test import TestCase

from trees.models import PlantedTree, Tree
from users.models import User


class UserTestClass(TestCase):

    fixtures = ["users", "accounts", "trees"]

    @classmethod
    def setUpTestData(cls):
        getcontext().prec = 6

        cls.cajuacu = Tree.objects.get(name="Cajuaçu")
        cls.floripa = (Decimal("-27.5969"), Decimal("-48.5495"))

        cls.andiroba = Tree.objects.get(name="Andiroba")
        cls.imbituba = (Decimal("-28.2405"), Decimal("-48.6703"))

        assert not PlantedTree.objects.all()

    def test_user_can_plant_a_tree(self):
        user = User.objects.get(username="teste-1")
        user.plant_tree(self.cajuacu, self.floripa)

        planted_tree = PlantedTree.objects.get(user_id=user.id, tree_id=self.cajuacu.id)
        print("planted_tree.location", planted_tree.location)
        print("self.floripa", self.floripa)
        assert planted_tree
        assert planted_tree.location == self.floripa

    def test_user_can_plant_multiple_trees(self):
        plants = [(self.cajuacu, self.floripa), (self.andiroba, self.imbituba)]

        user = User.objects.get(username="teste-2")
        user.plant_trees(plants)

        planted_tree = PlantedTree.objects.get(user_id=user.id, tree_id=self.cajuacu.id)

        assert planted_tree
        assert planted_tree.location == self.floripa

        planted_tree = PlantedTree.objects.get(
            user_id=user.id, tree_id=self.andiroba.id
        )

        assert planted_tree
        assert planted_tree.location == self.imbituba
