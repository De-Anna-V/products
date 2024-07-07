from rest_framework import serializers
from main.models import Review, Product



class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.IntegerField()



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'text', 'mark', 'created_at']

class ProductDetailsSerializer(serializers.ModelSerializer):
    
    #reviews = ReviewSerializer(many = True, read_only = True)
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 
                  #'reviews'
                  ]

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['reviews'] = list([ReviewSerializer(review).data for review in Review.objects.filter(product=instance)])

        return representation




