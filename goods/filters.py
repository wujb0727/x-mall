from django_filters import rest_framework

from goods.models import Good


class GoodsFilter(rest_framework.FilterSet):
    """
    商品的过滤类
    """
    # 对商品价格设置搜索的最大最小区间
    priceGt = rest_framework.NumberFilter(field_name='salePrice', lookup_expr='gte', help_text='最低价格')
    priceLte = rest_framework.NumberFilter(field_name='salePrice', lookup_expr='lte', help_text='最高价格')

    class Meta:
        model = Good
        fields = ('priceGt', 'priceLte')
