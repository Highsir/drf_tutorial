from rest_framework import serializers

from example.models import FileSys


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.HyperlinkedModelSerializer(view_name='file-info')

    class Meta:
        model = FileSys
        # fields = ['filename', 'uploader', 'file_size', 'first_upload_time', 'last_upload_time']
        fields = 'all'
