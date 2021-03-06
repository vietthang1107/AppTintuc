from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from news.models import New
from news.serializers import NewListSerializer, NewListSerializerFilter, NewListCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from news.models import Comment
from news.serializers import CommentCreateSerializer, CommentListSerializer, CommentListSerializerFilter


# Create your views here.

# New
class NewList(generics.GenericAPIView):
    queryset = New.objects.all()
    serializer_class = NewListSerializer
    serializer_create = NewListCreateSerializer

    ordering_fields = '__all__'
    filterset_class = NewListSerializerFilter

    @swagger_auto_schema(operation_summary='Danh sách bản tin', operation_description='Lấy danh sách bản tin')
    def get(self, request, *args, **kwargs):
        serializer_render = self.serializer_class
        queryset = self.filter_queryset(self.get_queryset().filter(**kwargs))
        serializer = serializer_render(queryset, many=True)
        return Response(serializer.data, status=200, content_type="application/json")

    @swagger_auto_schema(operation_summary='Thêm một bản tin', operation_description='Thêm một bản tin vào danh sách')
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

    def get_object(self, id):
        try:
            return New.objects.get(id=id)
        except New.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary='Chi tiết bản tin', operation_description='Lấy chi tiết bản tin theo id')
    def get(self, request, *args, **kwargs):
        serializer_render = self.serializer_class
        queryset = self.filter_queryset(self.get_queryset().filter(**kwargs))
        serializer = serializer_render(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary='Cập nhật bản tin', operation_description='Cập nhật thông tin bản tin')
    def put(self, request, id, format=None):
        new = self.get_object(id)
        serializer = NewListSerializer(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Xóa bản tin', operation_description='Xóa bản tin')
    def delete(self, request, id, format=None):
        new = self.get_object(id)
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Comment
class CommentList(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    serializer_create = CommentCreateSerializer

    ordering_fields = '__all__'
    filterset_class = CommentListSerializerFilter

    @swagger_auto_schema(operation_summary='Danh sách comment', operation_description='Lấy danh sách comment')
    def get(self, request, *args, **kwargs):
        serializer_render = self.serializer_class
        queryset = self.filter_queryset(self.get_queryset().filter(**kwargs))
        serializer = serializer_render(queryset, many=True)
        return Response(serializer.data, status=200, content_type="application/json")

    @swagger_auto_schema(operation_summary='Thêm một comment', operation_description='Thêm một comment vào tin tức')
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_create(data={**request.data, **kwargs})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
