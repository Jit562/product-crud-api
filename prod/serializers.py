from rest_framework.serializers import ModelSerializer
from prod.models import Category, Product


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category

        fields = ['id','category_name']


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product

        fields = '__all__'

        
class RetriveProductSerializer(ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Product

        fields = '__all__'




