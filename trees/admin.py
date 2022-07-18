from django.contrib import admin

from trees.models import PlantedTree, Tree


class PlantedTreeAdmin(admin.ModelAdmin):
    list_display = ("age", "planted_at", "tree", "user")


admin.site.register(Tree)
admin.site.register(PlantedTree, PlantedTreeAdmin)
