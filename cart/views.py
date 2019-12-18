from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from cart.models import Cart
from cart.serializers import ListCartSerializer, CartSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCartSerializer
        else:
            return CartSerializer

    @action(methods=['post'], detail=False)
    def edit_check_all(self, request):
        user = request.user.id
        checked = request.data['checked']
        cart_list = Cart.objects.filter(user=user)
        for cart in cart_list:
            cart.checked = checked
            cart.save()
        return Response({'success': True})

    @action(methods=['post'], detail=False)
    def del_cart_checked(self, request):
        user = request.user.id
        Cart.objects.filter(user=user, checked=True).all().delete()
        return Response({'success': True})
