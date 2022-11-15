from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MashinaSerializer
from .models import Mashina
# Create your views here

class MashinaViewSet(viewsets.ModelViewSet):
    queryset = Mashina.objects.all()
    serializer_class = MashinaSerializer