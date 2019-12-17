from django.urls import path

from rest_framework.routers import DefaultRouter

from account import views

router = DefaultRouter()
router.register('', views.UserViewSet, basename='user')
urlpatterns = router.urls

# urlpatterns = [
#     path('<username>/', views.UserDetail.as_view(), name='user-detail'),
#     path('', views.UserList.as_view(), name='user-list'),
# ]
