from rest_framework import serializers
from api.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for model Client
    """
    class Meta:
        model = Client
        fields = '__all__'

