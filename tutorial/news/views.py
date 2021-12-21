from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from news.models import New
from news.serializers import NewListSerializer, NewListSerializerFilter, NewListCreateSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.


class NewList(generics.GenericAPIView):
    queryset = New.objects.all()
    serializer_class = NewListSerializer
    serializer_create = NewListCreateSerializer

    ordering_fields = '__all__'
    filterset_class = NewListSerializerFilter

    @swagger_auto_schema(operation_summary='Danh sách bản tin', operation_description='Mô tả')
    def get(self, request, *args, **kwargs):
        serializer_render = self.serializer_class
        queryset = self.filter_queryset(self.get_queryset().filter(**kwargs))
        serializer = serializer_render(queryset, many=True)
        return Response(serializer.data, status=200, content_type="application/json")

    @swagger_auto_schema(operation_summary='Thêm một bản tin', operation_description='Mô tả')
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_create(data={**request.data, **kwargs})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewDetail(generics.GenericAPIView):
    queryset = New.objects.all()
    serializer_class = NewListSerializer
    ordering_fields = '__all__'
    filterset_class = NewListSerializerFilter

    def get_object(self, pk):
        try:
            return New.objects.get(pk=pk)
        except New.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary='Danh sách bản tin theo id', operation_description='Mô tả')
    def get(self, request, *args, **kwargs):
        serializer_render = self.serializer_class
        queryset = self.filter_queryset(self.get_queryset().filter(**kwargs))
        serializer = serializer_render(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary='Cập nhật bản tin', operation_description='Mô tả')
    def put(self, request, pk, format=None):
        new = self.get_object(pk)
        serializer = NewListSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Xóa bản tin', operation_description='Mô tả')
    def delete(self, request, pk, format=None):
        new = self.get_object(pk)
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
