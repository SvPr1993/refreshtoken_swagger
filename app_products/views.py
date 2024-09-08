from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from rest_framework.decorators import api_view, renderer_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


products = {
    "key_1": "Картошка",
    "key_2": "Ягоды",
    "key_3": "Овощи",
}


header_param = openapi.Parameter('products',openapi.IN_QUERY,description="Products List", type=openapi.IN_QUERY)


response_schema_dict = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
            "key1": "Картошка",
            "key_2": "Ягоды",
            "key_3": "Овощи,"
            }
        }
    ),}

class Products(APIView):

    @swagger_auto_schema(manual_parameters=[header_param], responses=response_schema_dict)
    def get(self, request):
        product_list = products
        return Response(product_list)

class MyTestAPIView(APIView):
    def post(self, request):
        return Response({"foo": "bar"})