from rest_framework import serializers
from api.models import Client, Product, Bill, BillProducts
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


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
