from django.urls import path, include

from .views import NinjaCreate

from rest_framework import urls

urlpatterns = [
    path('/signup', NinjaCreate.as_view()),
    path('/api-auth', include('rest_framework.urls')),
]
