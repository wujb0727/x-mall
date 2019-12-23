from rest_framework.routers import DefaultRouter

from order import views

router = DefaultRouter()
router.register('', views.OrderViewSet, basename='order')
urlpatterns = router.urls
