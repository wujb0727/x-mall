from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from account.models import User
from account.serializers import UserSerializer, NewUserSerializer, UserAvatarSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'
#     lookup_url_kwarg = 'username'
#
#     # def get(self, request, *args, **kwargs):
#     #     return self.retrieve(request, *args, **kwargs)
#     #
#     # def put(self, request, *args, **kwargs):
#     #     return self.update(request, *args, **kwargs)
#     #
#     # def patch(self, request, *args, **kwargs):
#     #     return self.partial_update(request, *args, **kwargs)
#     #
#     # def delete(self, request, *args, **kwargs):
#     #     return self.delete(request, *args, **kwargs)
#
#
# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return UserSerializer
#         elif self.request.method == 'POST':
#             return NewUserSerializer
#         return super().get_serializer_class()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    lookup_url_kwarg = 'username'

    def get_serializer_class(self):
        if self.action == 'create':
            return NewUserSerializer
        elif self.action == 'partial_update':
            return UserAvatarSerializer
        else:
            return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        user = User(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'username': serializer.data['username'],
                'token': token},
            status=status.HTTP_201_CREATED,
            headers=headers)

    def retrieve(self, request, *args, **kwargs):
        username = request.path.split('/')[3]
        instance = User.objects.get(Q(username=username) | Q(
            mobile=username) | Q(email=username))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(
                mobile=username) | Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist as e:
            return None
