from rest_framework import serializers
from api.models import Client, Product


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for model Client
    """
    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for model Client
    """
    class Meta:
        model = Product
        fields = '__all__'

