from django.shortcuts import get_object_or_404
from models import Recipe
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tag.models import Tag

from ..serializers import RecipeSerializer, TagSerializer


@api_view()
def recipe_api_list(request) -> Response:
    recipes = Recipe.objects.get_published()[:10]
    serializer = RecipeSerializer(
        instance=recipes,
        many=True,
        context={'request': request}
    )
    return Response(serializer.data)

@api_view()
def recipe_api_detail(request, pk) -> Response:
    recipes = get_object_or_404(
        Recipe.objects.get_published(),
        pk=pk
    )
    
    
    serializer = RecipeSerializer(
        instance=recipes,
        many=False,  # Add a comma here
        context={'request': request}    
    )
    return Response(serializer.data)

@api_view()
def tag_api_detail(request, pk) -> Response:
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request}    
    )
    return Response(serializer.data)
