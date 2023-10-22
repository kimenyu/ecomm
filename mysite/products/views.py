from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer



class ProductList(generics.ListCreateAPIView):
    """ProductList definition.

    Args:
        generics (ListCreateAPIView): ListCreateAPIView
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """ProductDetail definition.

    Args:
        generics (RetrieveUpdateDestroyAPIView): RetrieveUpdateDestroyAPIView
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    """CategoryList definition.

    Args:
        generics (ListCreateView): ListCreateAPIView
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """CategoryDetail definition.

    Args:
        generics (retrieveUpdatedestroy): it is a retrieve update destroy api view
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
