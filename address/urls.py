from rest_framework.routers import DefaultRouter

from address import views

router = DefaultRouter()
router.register('', views.AddressViewSet, basename='address')
urlpatterns = router.urls
