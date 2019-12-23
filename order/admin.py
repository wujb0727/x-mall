from django.contrib import admin

from order.models import Order, OrderGood


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_sn',
        'pay_status',
        'order_total',
        'address',
        'singer_name',
        'singer_mobile',
        'user']


@admin.register(OrderGood)
class OrderGoodAdmin(admin.ModelAdmin):
    list_display = ['good', 'order', 'good_num']
