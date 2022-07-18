from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from trees.models import PlantedTree


class PlantedTreeCreateView(LoginRequiredMixin, generic.CreateView):
    model = PlantedTree
    template_name = "trees/planted_tree_add.html"
    success_url = reverse_lazy("planted-tree-by-user-index")
    fields = ["age", "tree", "account"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
