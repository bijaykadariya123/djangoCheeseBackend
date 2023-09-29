from django.shortcuts import render

# Create your views here.
from .models import cheese
from rest_framework import viewsets, permissions
from .serializers import CheeseSerializer

class CheeseViewSet(viewsets.ModelViewSet):
    queryset = cheese.objects.all()
    serializer_class=CheeseSerializer
    permission_classes=[permissions.AllowAny]
