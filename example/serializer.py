from rest_framework import serializers

from example.models import FileSys, Comment
from snippets.serializers import UserSerializer


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.HyperlinkedModelSerializer(view_name='file-info')

    class Meta:
        model = FileSys
        # fields = ['filename', 'uploader', 'file_size', 'first_upload_time', 'last_upload_time']
        fields = 'all'


class CommentSerializer(serializers.Serializer):
    user = UserSerializer()
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
