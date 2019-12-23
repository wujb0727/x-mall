from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from goods.filters import GoodsFilter
from goods.models import Good, Category
from goods.serializers import GoodSerializer, GoodDetailSerializer


# 自定义分页类
class GoodPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'


class GoodListView(generics.ListAPIView):
    """
    商品列表
    """
    serializer_class = GoodSerializer
    pagination_class = GoodPageNumberPagination
    filter_backends = (DjangoFilterBackend,)  # 过滤配置
    filter_class = GoodsFilter
    authentication_classes = []

    def get_queryset(self):
        queryset = Good.objects.all()
        sort = self.request.query_params.get('sort', None)
        cid = self.request.query_params.get('cid', None)
        if sort == '1':
            queryset = queryset.order_by('salePrice')
        elif sort == '-1':
            queryset = queryset.order_by('-salePrice')

        if cid is not None:
            queryset = queryset.filter(category__parent_id=cid).all()
        return queryset


class GoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    商品详情
    """
    queryset = Good.objects.all()
    serializer_class = GoodDetailSerializer
    authentication_classes = []
