from django.urls import path, include

urlpatterns = [
    path('organization/', include('api.v1.organization.urls')),
]