from django.db import models
from django.db.models.signals import pre_save, post_delete
from rest_framework import serializers

from gecommerce.utils.signal_listener import auto_delete_file_on_delete, auto_delete_file_on_change

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(upload_to="./product")
  description = models.CharField(max_length=500)
  price = models.DecimalField(max_digits=12, decimal_places=2)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id',  'name', 'img', 'description', 'price')

post_delete(auto_delete_file_on_delete, Product)
pre_save(auto_delete_file_on_change, Product)