from django.urls import path

from account import views

urlpatterns = [
    path('<username>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.UserCreate.as_view(), name='user-create'),
]
