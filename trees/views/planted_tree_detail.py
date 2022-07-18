from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from trees_everywhere.middleware import get_current_user
from trees.models import PlantedTree


class PlantedTreeDetailView(LoginRequiredMixin, generic.DetailView):
    model = PlantedTree
    template_name = "trees/planted_tree_detail.html"

    def get_object(self, queryset=None):
        obj = super(PlantedTreeDetailView, self).get_object(queryset=queryset)
        if obj.user_id != get_current_user().id:
            raise PermissionDenied()
        return obj
