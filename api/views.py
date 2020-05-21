from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client, Product
from .serializers import ClientSerializer, ProductSerializer


class ClientView(APIView):
    """
    Class for manage the client
    """
    def get(self, request):
        clients = Client.objects.raw('SELECT * FROM api_client')
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_client = get_object_or_404(Client.objects.all(), pk=pk)
        data = request.data
        serializer = ClientSerializer(instance=saved_client, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "Client with id '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response({"message": "Client with id `{}` has been deleted.".format(pk)}, status=204)


class ProductView(APIView):
    """
    Class for manage Products
    """
    def get(self, request):
        products = Product.objects.raw('SELECT * FROM api_product')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        product_saved = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(instance=product_saved, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "Product with id '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"message": "Product with id `{}` has been deleted.".format(pk)}, status=204)


