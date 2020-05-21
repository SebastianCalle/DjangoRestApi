from rest_framework import serializers
from api.models import Client, Product, Bill, BillProducts


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


class BillProductsSerializer(serializers.ModelSerializer):
    """
    Serializer for model Bill and Products
    """
    class Meta:
        model = BillProducts
        fields = '__all__'

