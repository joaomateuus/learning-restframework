from rest_framework import viewsets
from core import models, serializers


class HeroViewSet(viewsets.ModelViewSet):
    queryset = models.Hero.objects.all()
    serializer_class = serializers.HeroSerializer


class PowerSerializer(viewsets.ModelViewSet):
    queryset = models.Power.objects.all()
    serializer_class = serializers.PowerSerializer
