from rest_framework.pagination import PageNumberPagination


# 自定义分页类
class GoodPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'
