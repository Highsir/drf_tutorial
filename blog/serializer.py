from abc import ABC
from datetime import date

from django.db import models
from rest_framework import serializers
from blog.models import Blog, Entry, Author


class BlogSerializer(serializers.Serializer, ABC):
    name = serializers.CharField(max_length=100)
    tagline = serializers.TextField()

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.tagline = validated_data.get('name', instance.tagline)
        instance.save()
        return instance


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = 'all'


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = 'all'
