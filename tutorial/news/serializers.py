from django.db.models import fields, JSONField
from rest_framework import serializers
from news.models import New, Comment
from django_filters import rest_framework as filters


# New
class NewListSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()

    class Meta:
        model = New
        fields = ('id', 'comment', 'date_created',
                  'title', 'description', 'author')

    def get_comment(self, obj):
        comments = Comment.objects.filter(new_id=obj.id)
        result = []
        if comments:
            for comment in comments:
                result.append({
                    'user_comment': comment.user_comment,
                    'content': comment.content,
                })
        return result


class NewListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('title', 'description', 'author', )


class NewListSerializerFilter(filters.FilterSet):
    class Meta:
        model = New
        fields = ('id', 'title', 'description', 'author')


# Comment
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'new', 'date_created', 'content', 'user_comment')


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'user_comment', 'new')


class CommentListSerializerFilter(filters.FilterSet):
    class Meta:
        model = Comment
        fields = ('id', 'user_comment')
