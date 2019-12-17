from django.db import models


class Address(models.Model):
    name = models.CharField(verbose_name='名称', max_length=20)
    tel = models.CharField(verbose_name='电话', max_length=11)
    address = models.CharField(verbose_name='地址', max_length=150)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    user_id = models.ForeignKey('account.User', verbose_name='用户', on_delete=models.CASCADE)
    is_default = models.BooleanField(verbose_name='是否为默认地址', default=False)

    class Meta:
        verbose_name = '地址表'
        verbose_name_plural = verbose_name
        ordering = ('-is_default',)

    def __str__(self):
        return self.name
