from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class NavList(models.Model):
    name = models.CharField(verbose_name='名称', max_length=120)
    panelId = models.PositiveIntegerField(verbose_name='面板ID', default=0)
    type = models.PositiveIntegerField(verbose_name='类型', default=1)
    sortOrder = models.PositiveIntegerField(verbose_name='排序')
    fullUrl = models.CharField(verbose_name='跳转链接', max_length=120)
    picUrl = models.CharField(max_length=120, null=True, blank=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '首页导航栏'
        verbose_name_plural = verbose_name
        ordering = ('sortOrder',)

    def __str__(self):
        return self.name


class Panel(models.Model):
    name = models.CharField(verbose_name='名称', max_length=120)
    type = models.IntegerField(verbose_name='类型')
    sort_order = models.IntegerField(verbose_name='排序')
    position = models.IntegerField(verbose_name='位置', default=0)
    limit_num = models.IntegerField(verbose_name='限制数量')
    status = models.IntegerField(verbose_name='状态', default=1)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = '首页面板栏'
        verbose_name_plural = verbose_name
        # ordering = ('sortOrder',)

    def __str__(self):
        return self.name


class PanelContents(models.Model):
    type = models.IntegerField(verbose_name='类型', default=0)
    sort_order = models.IntegerField(verbose_name='排序')
    fullUrl = models.CharField(verbose_name='跳转链接', max_length=120, null=True, blank=True)
    picUrl = RichTextUploadingField(verbose_name='图片1', null=True, blank=True)
    picUrl2 = RichTextUploadingField(verbose_name='图片2', null=True, blank=True)
    picUrl3 = RichTextUploadingField(verbose_name='图片3', null=True, blank=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    panelId = models.ForeignKey('home.Panel', verbose_name='首页面板', related_name='panelContents',
                                on_delete=models.CASCADE)
    productId = models.ForeignKey('goods.Good', verbose_name='商品', related_name='panel_contents',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = '面板详情'
        verbose_name_plural = verbose_name
        # ordering = ('sortOrder',)

    def __str__(self):
        return self.panelId.name
