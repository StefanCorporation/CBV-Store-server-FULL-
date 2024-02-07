from django.urls import path, include
from api import views
from rest_framework import routers


app_name = 'api'


router = routers.DefaultRouter()
router.register(r'products', views.ProductModelViewSet)
router.register(r'baskets', views.BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]