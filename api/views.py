from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client, Product, Bill, BillProducts
from .serializers import ClientSerializer, ProductSerializer, BillSerializer, BillProductsSerializer, UserSerializer


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


class BillView(APIView):
    """
    Class for manage Bill
    """
    def get(self, request):
        bills = Bill.objects.raw('SELECT * FROM api_bill')
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        bill_saved = get_object_or_404(Bill.objects.all(), pk=pk)
        data = request.data
        serializer = BillSerializer(instance=bill_saved, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "Bill with id '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        bill = get_object_or_404(Bill.objects.all(), pk=pk)
        bill.delete()
        return Response({"message": "Bill with id `{}` has been deleted.".format(pk)}, status=204)


class BillByClientIdView(APIView):
    """
    Class for manage Bill by client id
    """
    def get(self, request, pk):
        bills = Bill.objects.raw('SELECT * FROM api_bill WHERE client_id_id = %s', [pk])
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)


class ProductsByBillView(APIView):
    """
    Class to manage relationship of products to bill
    """
    def get(self, request, pk):
        bills = BillProducts.objects.raw('SELECT * FROM api_billproducts WHERE bill_id_id = %s', [pk])
        serializer = BillProductsSerializer(bills, many=True)
        list_products = []
        for obj in serializer.data:
            product = Product.objects.raw('SELECT * FROM api_product WHERE id = %s', [obj.get('product_id')])
            product_serializer = ProductSerializer(product, many=True)
            list_products.append(product_serializer.data)
        return Response(list_products)


class BillByProductView(APIView):
    """
    Class to manage relationship of bill to product
    """
    def get(self, request, pk):
        prodcut = BillProducts.objects.raw('SELECT * FROM api_billproducts WHERE product_id_id = %s', [pk])
        serializer = BillProductsSerializer(prodcut, many=True)
        list_bills = []
        for obj in serializer.data:
            bill = Bill.objects.raw('SELECT * FROM api_bill WHERE id = %s', [obj.get('bill_id')])
            bill_serializer = BillSerializer(bill, many=True)
            list_bills.append(bill_serializer.data)
        return Response(list_bills)


class BillProductView(APIView):
    """
    Class to manage relationship of bill to product
    """
    def get(self, request):
        bills_products = BillProducts.objects.raw('SELECT * FROM api_billproducts')
        serializer = BillProductsSerializer(bills_products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BillProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        bill_product_saved = get_object_or_404(BillProducts.objects.all(), pk=pk)
        data = request.data
        serializer = BillProductsSerializer(instance=bill_product_saved, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"success": "BIll-Product with id '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        bill_product = get_object_or_404(BillProducts.objects.all(), pk=pk)
        bill_product.delete()
        return Response({"message": "Bill-Product with id `{}` has been deleted.".format(pk)}, status=204)


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
