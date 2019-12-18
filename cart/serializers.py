from rest_framework import serializers

from cart.models import Cart
from goods.models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ['id', 'productName', 'subTitle', 'productImageBig', 'salePrice']


class ListCartSerializer(serializers.ModelSerializer):
    good = GoodSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        instance, created = Cart.objects.update_or_create(**validated_data)
        return instance
