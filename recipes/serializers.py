from django.contrib.auth.models import User
from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugFild()

class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_public')
<<<<<<< HEAD
    preparetion = serializers.SerializerMethodField(method_name='any_method')
    
    category =  serializers.StringRelatedField()
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )
    
    tag_objects = TagSerializer(
        many=True,
        source='tags'
    )
    
    tag_links =  serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        queryset=Tag.objects.all(),
        read_only=True,
        view_name='recipes:recipes_api_v2_tag'
    )
    
    def any_method(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
     
=======
    preparation = serializers.SerializerMethodField(method_name='any_method')

    def any_method(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
>>>>>>> refs/remotes/origin/Function_Base_View
    