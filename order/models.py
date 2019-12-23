import random
import uuid

from django.db import models
from django.utils.timezone import now

from xmall.settings import ORDER_TIMEOUT


def generate_order_sn():
    order_id = now().strftime('%Y%m%d%H%M%S%f')
    seeds = '0123456789'
    random_list = []
    for i in range(6):
        random_list.append(random.choice(seeds))
    return order_id + ''.join(random_list)


def generate_timeout():
    return now() + ORDER_TIMEOUT


class Order(models.Model):
    STATUS_UNPAY = '1'
    STATUS_UNDELIVER = '2'
    STATUS_DELIVER = '3'
    STATUS_ACHIEVE = '4'
    STATUS_EXPIRED = '5'
    STATUS_CANCEL = '6'

    STATUS_CHOICES = (
        (STATUS_UNPAY, '待支付'),
        (STATUS_UNDELIVER, '待发货'),
        (STATUS_DELIVER, '待收货'),
        (STATUS_ACHIEVE, '已收货'),
        (STATUS_EXPIRED, '交易关闭'),
        (STATUS_CANCEL, '支付失败'),
    )
    order_sn = models.CharField(
        verbose_name='订单编号',
        max_length=30,
        unique=True,
        default=generate_order_sn,
        editable=False)
    trade_no = models.CharField(
        verbose_name='交易号',
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        editable=False
    )
    pay_status = models.CharField(
        verbose_name='付款状态',
        max_length=30,
        choices=STATUS_CHOICES,
        default=STATUS_UNPAY)
    post_script = models.CharField(
        verbose_name='留言',
        max_length=200,
        null=True,
        blank=True)
    order_total = models.DecimalField(
        verbose_name='订单总价',
        max_digits=10,
        decimal_places=2)
    address = models.CharField(verbose_name='收货地址', max_length=100)
    singer_name = models.CharField(verbose_name='收货人姓名', max_length=20)
    singer_mobile = models.CharField(verbose_name='收货人电话', max_length=11)
    user = models.ForeignKey(
        'account.User',
        verbose_name='用户',
        on_delete=models.CASCADE,
        related_name='order')
    created = models.DateTimeField(verbose_name='订单创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='订单更新时间', auto_now=True)
    close_time = models.DateTimeField(
        verbose_name='订单过期时间',
        default=generate_timeout)

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ('-created',)

    def __str__(self):
        return self.order_sn


class OrderGood(models.Model):
    good_num = models.PositiveIntegerField(verbose_name='商品数量')
    price = models.DecimalField(
        verbose_name='价格',
        max_digits=10,
        decimal_places=2,
        default=0)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    order = models.ForeignKey(
        'order.Order',
        verbose_name='订单',
        on_delete=models.CASCADE,
        related_name='goods')
    good = models.ForeignKey(
        'goods.Good',
        verbose_name='商品',
        on_delete=models.CASCADE,
        related_name='order')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.good.productName
