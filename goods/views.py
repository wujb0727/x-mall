from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from goods.filters import GoodsFilter
from goods.models import Good
from goods.paginations import GoodPageNumberPagination
from goods.serializers import GoodSerializer, GoodDetailSerializer


class GoodListView(generics.ListAPIView):
    """
    商品列表
    """
    serializer_class = GoodSerializer
    pagination_class = GoodPageNumberPagination
    filter_backends = (DjangoFilterBackend,)  # 过滤配置
    filter_class = GoodsFilter

    def get_queryset(self):
        queryset = Good.objects.all()
        sort = self.request.query_params.get('sort', None)
        if sort == '1':
            queryset = queryset.order_by('salePrice')
        elif sort == '-1':
            queryset = queryset.order_by('-salePrice')
        return queryset


class GoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    商品详情
    """
    queryset = Good.objects.all()
    serializer_class = GoodDetailSerializer
