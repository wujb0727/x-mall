from django.db import models


class Good(models.Model):
    salePrice = models.DecimalField(verbose_name='销售价格', max_digits=10, decimal_places=2)
    productName = models.CharField(verbose_name='产品名称', max_length=50)
    subTitle = models.CharField(verbose_name='字幕', max_length=200, null=True, blank=True)
    productImageBig = models.ImageField(verbose_name='商品图片', upload_to='goods/good/%Y/%m/%d')
    detail = models.TextField(verbose_name='商品详情', null=True, blank=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    category_id = models.ForeignKey('goods.Category', verbose_name='商品分类', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.productName


class GoodImage(models.Model):
    image = models.ImageField(verbose_name='图片', upload_to='goods/good-image/%Y/%m/%d')
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    good_id = models.ForeignKey('goods.Good', verbose_name='商品', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '商品图片表'
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(verbose_name='名称', max_length=50)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    slug = models.CharField(max_length=120, null=True, blank=True)
    parent_id = models.ForeignKey('goods.Category', verbose_name='父级分类', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
