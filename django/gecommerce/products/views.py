from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import Product, ProductSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Create your views here.
def index(request):
  return HttpResponse(render(request, "./index.html"))