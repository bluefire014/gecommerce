from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductsViewSet)

urlpatterns = [
    path('', views.index),
    path('', include(router.urls)),
]
