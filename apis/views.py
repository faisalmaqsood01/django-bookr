from .models import Product
from .serializers import (
    ProductSerializer)
from rest_framework import filters, permissions
from rest_framework import generics
from .pagination_class import StandardResultsSetPagination


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = StandardResultsSetPagination
