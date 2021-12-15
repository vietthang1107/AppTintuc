from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from news.models import New
from news.serializers import NewSerializer

# Create your views here.


class NewList(APIView):
    def get(self, request, format=None):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewDetail(APIView):
    def get_object(self, pk):
        try:
            return New.objects.get(pk=pk)
        except New.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        new = self.get_object(pk)
        serializer = NewSerializer(new)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        new = self.get_object(pk)
        serializer = NewSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        new = self.get_object(pk)
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
