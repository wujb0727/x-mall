from django.urls import path
from rest_framework.routers import DefaultRouter

from cart import views

router = DefaultRouter()
router.register('', views.CartViewSet, basename='cart')
urlpatterns = router.urls

