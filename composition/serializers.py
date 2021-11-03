from rest_framework import serializers
from .models import (
    Canton, 
    Commune, 
    Region, 
    Prefecture, 
    Village,
    Quartier
)

class CantonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Canton
        exclude = ['created_at', 'updated_at']


class CommuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commune
        exclude = ['created_at', 'updated_at']

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        exclude = ['created_at', 'updated_at']

class PrefectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prefecture
        exclude = ['created_at', 'updated_at']

class VillageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Village
        exclude = ['created_at', 'updated_at']

class QuartierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quartier
        exclude = ['created_at', 'updated_at']