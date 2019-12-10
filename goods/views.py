from django.shortcuts import render
from rest_framework import mixins, generics

from goods.models import Good
from goods.serializers import GoodSerializer


class GoodList(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
