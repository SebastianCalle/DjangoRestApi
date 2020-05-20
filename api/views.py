from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer


# Create your views here.
class ClientView(APIView):
    # View for list and create client
    def get(self, request):
        clients = Client.objects.all()
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
            client_saved = serializer.save()
        return Response({"success": "Client with id '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        client = get_object_or_404(Client.objects.all(), pk=pk)
        client.delete()
        return Response({"message": "Client with id `{}` has been deleted.".format(pk)}, status=204)


