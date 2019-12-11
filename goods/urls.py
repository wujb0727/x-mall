from django.urls import path

from goods import views

urlpatterns = [
    path('', views.GoodListView.as_view(), name='good-list'),
    path('<pk>/', views.GoodDetailView.as_view(), name='good-detail'),
]
