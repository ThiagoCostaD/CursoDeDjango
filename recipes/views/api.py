from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def recipe_api_list(request) -> Response:
    return Response('ok')
