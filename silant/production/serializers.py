from rest_framework import serializers
from .models import Mashina

class MashinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mashina
        fields = ('zavodsk_nomer', 'model_tech', 'model_dvig', 'nomer_dvig')