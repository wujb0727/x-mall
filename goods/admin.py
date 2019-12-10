from django.contrib import admin

from goods.models import Good, Category, GoodImage


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['salePrice', 'productName', 'category_id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_id']


@admin.register(GoodImage)
class GoodImageAdmin(admin.ModelAdmin):
    pass
