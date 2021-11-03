from rest_framework import serializers
from .models import Leader

class LeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leader
        exclude = ['created_at', 'updated_at']