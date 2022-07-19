from django.test import TestCase, Client
from django.urls import reverse

from trees.models import PlantedTree
from users.models import User
from trees_everywhere.middleware import set_current_accounts, set_current_user


class PlantedTreesTestClass(TestCase):

    fixtures = ["users", "accounts", "trees", "planted_trees"]

    @classmethod
    def setUpTestData(cls):
        user = User.objects.get(username="teste-1")
        set_current_user(user)
        set_current_accounts(user.accounts)
        cls.planted_trees_by_user = PlantedTree.objects.by_user().order_by("-id")
        cls.planted_trees_by_accounts = PlantedTree.objects.by_accounts().order_by(
            "-id"
        )

    def setUp(self):
        self.client = Client()
        self.client.login(username="teste-1", password="Admin-123")

    def test_planted_trees_by_user_is_rendered(self):
        url = reverse("planted-tree-by-user-index")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trees/planted_trees_index.html", "base.html")
        self.assertIn("planted_trees_list", response.context_data)
        self.assertQuerysetEqual(
            response.context_data["planted_trees_list"], self.planted_trees_by_user
        )

    def test_planted_trees_detail_return_forbidden_if_accessed_by_other_user(self):
        url = reverse("planted-tree-detail", kwargs={"pk": 3})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 403)

    def test_planted_trees_by_account_is_rendered(self):
        url = reverse("planted-tree-by-accounts-index")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "trees/planted_trees_index.html", "base.html")
        self.assertIn("planted_trees_list", response.context_data)
        self.assertQuerysetEqual(
            response.context_data["planted_trees_list"], self.planted_trees_by_accounts
        )
