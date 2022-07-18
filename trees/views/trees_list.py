from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from trees.models import Tree


class TreesListView(LoginRequiredMixin, generic.ListView):
    template_name = "trees/tree_index.html"
    context_object_name = "trees_list"

    def get_queryset(self):
        return Tree.objects.order_by("-id")
