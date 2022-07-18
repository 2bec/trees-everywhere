from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from trees.models import Tree


class TreeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tree
    template_name = "trees/tree_detail.html"
