from rest_framework import serializers
from news.models import New


# class NewSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(
#         required=False, allow_blank=True, max_length=100)
#     description = serializers.CharField()
#     author = serializers.CharField()

#     def create(self, validated_data):
#         return New.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.author = validated_data.get('author', instance.author)
#         instance.save()
#         return instance

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ['id', 'title', 'description', 'author']
