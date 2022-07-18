from django.db import models

from trees_everywhere.middleware import get_current_accounts, get_current_user


class PlantedTreesManager(models.Manager):
    def by_accounts(self):
        return (
            super(PlantedTreesManager, self)
            .get_queryset()
            .filter(account_id__in=get_current_accounts().all())
        )

    def by_user(self):
        return (
            super(PlantedTreesManager, self)
            .get_queryset()
            .filter(user_id=get_current_user().id)
        )
