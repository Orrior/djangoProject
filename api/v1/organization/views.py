# business logic
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from djangoProject.authentication import ExampleAuthentication
from organization.models import Organization
from . import serializer


class OrganizationAPI(ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = serializer.OrganizationSerializer
    authentication_classes = (TokenAuthentication, ExampleAuthentication,)  # specify this authentication class in your view
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({"status": True,
                         "message": "User Added!",
                         "data": serializer.data}
                        , status=status.HTTP_201_CREATED, headers=headers)


class OrganizationRetrieveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.OrganizationSerializer
    queryset = Organization.objects.all()
    authentication_classes = (TokenAuthentication, ExampleAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(id=self.kwargs.get("pk", None))

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"status": True, "message": "User has been Deleted!"},
                        status=status.HTTP_200_OK)
