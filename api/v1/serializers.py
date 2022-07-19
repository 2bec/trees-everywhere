from rest_framework import serializers

from trees.models import PlantedTree


class PlantedTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantedTree
        fields = ("age", "tree", "location", "planted_at")
