from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(verbose_name='移动电话', max_length=20, blank=True)
    image = models.ImageField(verbose_name='图片', upload_to='account/avatar/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
