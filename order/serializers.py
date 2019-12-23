from rest_framework import serializers

from goods.models import Good
from order.models import Order, OrderGood


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'salePrice', 'productName', 'productImageBig']


class OrderGoodSerializer(serializers.ModelSerializer):
    good = GoodSerializer()

    class Meta:
        model = OrderGood
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    goods = OrderGoodSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
