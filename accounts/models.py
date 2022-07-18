from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    active = models.BooleanField(default=False)
    users = models.ManyToManyField("users.User", related_name="accounts")

    def __str__(self):
        return self.name
