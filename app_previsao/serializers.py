from rest_framework import serializers
from .models import PrevisaoModel

class PrevisaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrevisaoModel
        fields = "__all__"
