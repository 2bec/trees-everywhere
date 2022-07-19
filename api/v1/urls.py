from django.urls import path, include
from rest_framework import routers

from .views import PlantedTreeViewSet


planted_tree_router = routers.SimpleRouter()
planted_tree_router.register("", PlantedTreeViewSet, basename="planted-trees-by-user")


urlpatterns = [path("trees/planted/", include(planted_tree_router.urls))]
