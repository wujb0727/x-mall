from django.urls import path

from goods import views

urlpatterns = [
    path('', views.GoodList.as_view(), name='good-list'),
]
