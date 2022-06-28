from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import NinjaSerializer
from .models import User


class NinjaCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = NinjaSerializer
    permission_classes = [AllowAny]

