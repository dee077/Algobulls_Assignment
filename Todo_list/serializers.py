from rest_framework import serializers
from .models import ToDoItem,Tag
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
    def to_internal_value(self, data):
        name = data.get('name')

        if name:
            try:
                # Try to retrieve an existing tag with the same name
                tag = Tag.objects.get(name=name)
                return {'name': tag.name}
            except Tag.DoesNotExist:
                # If the tag doesn't exist, create a new one
                return {'name': name}

        return super().to_internal_value(data)

class ToDoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        todo = ToDoItem.objects.create(**validated_data)

        for tag_data in tags_data:
            tag_name = tag_data.get('name')
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            todo.tags.add(tag)

        return todo

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance = super().update(instance, validated_data)

        for tag_data in tags_data:
            tag_name = tag_data.get('name')
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

        return instance
    class Meta:
        model = ToDoItem
        fields = '__all__'
    
    