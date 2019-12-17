from django.urls import path

from home import views

urlpatterns = [
    path('navList/', views.NavListView.as_view(), name='nav-list'),
    path('home/', views.HomeView.as_view(), name='home-home')
]
