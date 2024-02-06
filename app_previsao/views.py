from django.shortcuts import render
from rest_framework import viewsets
from app_previsao.serializers import PrevisaoSerializer
from app_previsao.models import PrevisaoModel

class PrevisaoViewSet(viewsets.ModelViewSet):
    serializer_class= PrevisaoSerializer
    queryset = PrevisaoModel.objects.all()
