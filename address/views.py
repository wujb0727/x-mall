from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from address.models import Address
from address.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        request.data['user_id'] = request.user.id
        return super().create(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         self.perform_destroy(instance)
    #     except Exception as e:
    #         return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({'success': True}, status=status.HTTP_204_NO_CONTENT)
