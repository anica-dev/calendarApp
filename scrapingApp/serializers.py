from rest_framework import serializers
from .models import ScrapedData

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields='__all__'