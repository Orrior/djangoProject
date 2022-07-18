# my_app/authentication.py
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class ExampleAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        if(request.META.get("HTTP_SKEY") == "skeywordtest123"):

            return (User.objects.all().first(), None)
        else:
            return None
