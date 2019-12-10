from rest_framework import serializers

from goods.models import Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = (
            'id', 'salePrice', 'productName', 'subTitle', 'productImageBig', 'detail', 'created', 'updated',
            'category_id')
        # fields = ('__all__',)
