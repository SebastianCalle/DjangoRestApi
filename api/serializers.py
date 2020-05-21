from rest_framework import serializers
from api.models import Client, Product, Bill


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for model Client
    """
    class Meta:
        model = Client
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for model Product
    """
    class Meta:
        model = Product
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    """
    Serializer for model Bill
    """
    class Meta:
        model = Bill
        fields = '__all__'

