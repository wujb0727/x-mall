from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.models import User
from goods.models import Good
from order.models import Order, OrderGood
from order.serializers import OrderSerializer


# 自定义分页类
class OrderPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'size'


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPageNumberPagination
    lookup_field = 'order_sn'
    lookup_url_kwarg = 'order_sn'

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        order_data = serializer.data
        order_data['user'] = User.objects.get(id=serializer.data['user'])
        order = Order.objects.create(**order_data)
        for item in data['goods']:
            item.pop('checked')
            item.pop('user')
            item.pop('id')
            item['good'] = Good.objects.get(id=item['good']['id'])
            item['order'] = order
            OrderGood.objects.create(**item)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers)
