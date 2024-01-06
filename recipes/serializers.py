from django.contrib.auth.models import User
from rest_framework import serializers

from tag.models import Tag

from .models import Recipe


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'slug',
        ]

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'description',
            'public',
            'category',
            'author',
            'tags',
            'tag_objects',
            'tag_links',
        ]
    
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(
        source='is_public',
        read_only=True,
    )

    preparetion = serializers.SerializerMethodField(
        method_name='any_method',
        read_only=True,
    )
    
    category =  serializers.StringRelatedField(read_only=True,)
        
    tag_objects = TagSerializer(
        many=True,
        source='tags',
        read_only=True,
    )
    
    tag_links =  serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        read_only=True,
        view_name='recipes:recipes_api_v2_tag'
    )
    
    def any_method(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
     

    preparation = serializers.SerializerMethodField(method_name='any_method')

    def any_method(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'

    