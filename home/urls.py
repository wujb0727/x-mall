from django.urls import path

from home import views

urlpatterns = [
    path('', views.NavListView.as_view(), name='nav-list'),
]
