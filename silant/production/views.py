from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MashinaSerializer
from .models import Mashina
# Create your views here

class MashinaView(viewsets.ModelViewSet):
    serializer_class = MashinaSerializer
    queryset = Mashina.objects.all()