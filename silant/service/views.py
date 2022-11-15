from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServisSerializer
from .models import Servis
# Create your views here

class ServisViewSet(viewsets.ModelViewSet):
    queryset = Servis.objects.all()
    serializer_class = ServisSerializer