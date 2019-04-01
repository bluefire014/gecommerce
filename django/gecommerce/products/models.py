from django.db import models
from rest_framework import serializers

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(upload_to="./product")
  description = models.CharField(max_length=500)
  price = models.DecimalField(max_digits=12, decimal_places=2)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'img', 'description', 'price')