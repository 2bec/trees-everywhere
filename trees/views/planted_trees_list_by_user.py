from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from trees.models import PlantedTree


class PlantedTreeListView(LoginRequiredMixin, generic.ListView):
    template_name = "trees/planted_trees_index.html"
    context_object_name = "planted_trees_list"

    def get_queryset(self):
        return PlantedTree.objects.by_user().order_by("-id")
