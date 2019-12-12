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
