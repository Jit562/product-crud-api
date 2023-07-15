from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from prod.models import  Product
from prod.serializers import ProductSerializer, RetriveProductSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from prod.pagination import StandardResultsSetPagination


# Create your views here.

class ProductViews(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination


class ProductAdd(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, format = None):

        category = self.request.query_params.get('category')

        if category:
            queryset = Product.objects.filter(category__category_name = category)

        else:
            queryset = Product.objects.all()

        serializer = RetriveProductSerializer(queryset, many=True)

        return Response({'count':len(serializer.data), 'data':serializer.data})
    
    
    def post(self, request, format=None):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ProductDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        try:
            product = Product.objects.get(id=pk)
            serializer = RetriveProductSerializer(product)

            return Response(serializer.data)
        except:
            return Response({'status':"Product is not availbe this id please search next id."})
        
        

    def put(self, request, pk, format=None):

        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):

        product = Product.objects.get(id=pk)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class Registerdemo(APIView):

    def post(self, request, format=None):

        username = request.data['username']
        password = request.data['password']

        user = User(username=username)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        
        return Response({
            'success':'Account is created',
            'user_id':user.id, 
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            })

