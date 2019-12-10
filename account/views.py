from django.shortcuts import render
from rest_framework import generics, mixins

from account.models import User
from account.serializers import UserSerializer, NewUserSerializer


class UserDetail(generics.GenericAPIView, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class UserCreate(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = NewUserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
