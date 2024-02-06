from multiprocessing.managers import BaseManager

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from recipes.serializers import RecipeSerializer
from tag.models import Tag

from ..models import Recipe


class RecipeAPIv2Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param: str = 'page_size'
    max_page_size = 100

class RecipeAPIv2List(ListCreateAPIView):

    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = PageNumberPagination

class RecipeAPIv2Detail(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.get_published()
    serializer_class = RecipeSerializer
    pagination_class = PageNumberPagination

    def partial_update(self, request, *args, **kwargs) -> Response:
        pk = kwargs.get('pk')
        recipe: BaseManager[Recipe] = Recipe.objects.filter(pk=pk).first()
        serializers = RecipeSerializer(
            instance=recipe,
            data=request.data,
            many=False,
            context={'request': request},
            partial=True
            )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view()
def tag_api_detail(request, pk):
    tag = get_object_or_404(
        Tag.objects.all(),
        pk=pk
    )
    serializer = TagSerializer(
        instance=tag,
        many=False,
        context={'request': request},
    )
    return Response(serializer.data)
