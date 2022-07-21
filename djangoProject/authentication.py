# my_app/authentication.py
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        password = "asdf"  # Make password more distinctive
        if request.META.get("HTTP_SKEY") == password:
            # return (User.objects.all().first(), None)
            user = User.objects.first()
            return (user, None)
        else:
            return None
