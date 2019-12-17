from django.shortcuts import render

from rest_framework import generics

from home.models import NavList, Panel
from home.serializers import NavListSerializer, PanelSerializer


class NavListView(generics.ListAPIView):
    queryset = NavList.objects.all()
    serializer_class = NavListSerializer
    authentication_classes = []


class HomeView(generics.ListAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
    authentication_classes = []
