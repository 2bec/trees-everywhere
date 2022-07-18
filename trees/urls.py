from django.urls import path

from .views import (
    trees_list,
    tree_detail,
    planted_trees_list_by_user,
    planted_trees_list_by_accounts,
    planted_tree_detail,
    create_planted_trees,
)

urlpatterns = [
    path("", trees_list.TreesListView.as_view(), name="tree-index"),
    path("<int:pk>/", tree_detail.TreeDetailView.as_view(), name="tree-detail"),
    path(
        "planted/",
        planted_trees_list_by_user.PlantedTreeListView.as_view(),
        name="planted-tree-by-user-index",
    ),
    path(
        "planted/by-accounts/",
        planted_trees_list_by_accounts.PlantedTreeListByAccountView.as_view(),
        name="planted-tree-by-accounts-index",
    ),
    path(
        "planted/add/",
        create_planted_trees.PlantedTreeCreateView.as_view(),
        name="planted-tree-add",
    ),
    path(
        "planted/<int:pk>/",
        planted_tree_detail.PlantedTreeDetailView.as_view(),
        name="planted-tree-detail",
    ),
]
