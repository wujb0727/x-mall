from django.db import models


class CartManager(models.Manager):
    def update_or_create(self, good_num=1, **kwargs):
        cart, created = self.get_or_create(**kwargs)
        if created:
            cart.good_num = good_num
        else:
            cart.good_num += good_num
        cart.save()
        return cart, created


class Cart(models.Model):
    checked = models.BooleanField(verbose_name='是否被选中', default=True)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    good = models.ForeignKey('goods.Good', verbose_name='商品', on_delete=models.CASCADE, related_name='cart')
    user = models.ForeignKey('account.User', verbose_name='用户', on_delete=models.CASCADE, related_name='cart')
    good_num = models.PositiveIntegerField(verbose_name='商品数量', default=1)

    objects = CartManager()

    class Meta:
        # unique_together = ['user', 'good']
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
