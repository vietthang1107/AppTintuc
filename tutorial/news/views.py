from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from news.models import New
from news.serializers import NewSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def new_list(request):
    if request.method == 'GET':
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        return Response(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = NewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def new_detail(request, pk):
    try:
        new = New.objects.get(pk=pk)
    except New.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewSerializer(new)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
