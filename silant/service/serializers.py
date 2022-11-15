from rest_framework import serializers
from .models import Servis

class ServisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servis
        fields = ('nazvanie', 'opisanie')