from rest_framework import serializers
from .models import ProfModel

class ProfSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProfModel
        fields='__all__'