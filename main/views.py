from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from main.models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    serialised_products = ProductListSerializer(products, many = True)
    return Response(serialised_products.data)

@api_view(['GET'])
def reviews_view(request):
    reviewss = Review.objects.all()
    serialised_reviewss = ReviewSerializer(reviewss, many = True)
    return Response(serialised_reviewss.data)

@api_view(['GET'])
def reviews_list_view(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product = product)
    serialised_reviews = ReviewSerializer(reviews, many = True)
    return Response(serialised_reviews.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        serialised_product = ProductDetailsSerializer(product)
        return Response(serialised_product.data)
    


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
