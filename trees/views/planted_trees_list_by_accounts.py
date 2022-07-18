from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from trees_everywhere.middleware import get_current_accounts
from trees.models import PlantedTree


class PlantedTreeListByAccountView(LoginRequiredMixin, generic.ListView):
    template_name = "trees/planted_trees_index.html"
    context_object_name = "planted_trees_list"

    def get_queryset(self):
        return PlantedTree.objects.by_accounts().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = ", ".join(
            account.name for account in get_current_accounts().all()
        )
        return context
