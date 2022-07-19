from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from trees.models import PlantedTree
from .serializers import PlantedTreeSerializer


class PlantedTreeViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    Return a list of all published articles ordered by date.
    """

    permissions_classes = (IsAuthenticated,)
    serializer_class = PlantedTreeSerializer

    def get_queryset(self):
        return PlantedTree.objects.by_user()
