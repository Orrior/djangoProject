import rest_framework.authtoken.models
from django.db import models


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(TimestampModel):
    email = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.email

