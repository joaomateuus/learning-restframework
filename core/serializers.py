from rest_framework import serializers
from core import models


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hero
        fields = '__all__'


class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Power
        fields = '__all__'
