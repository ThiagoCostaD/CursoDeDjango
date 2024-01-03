from django.contrib.auth.models import User
from rest_framework import serializers
from tags.models import Tag


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_public')
    preparetion = serializers.SerializerMethodField(method_name='any_method')
    
    category =  serializers.StringRelatedField()
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all()
    )
    
    def any_method(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
    
    