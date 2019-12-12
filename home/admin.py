from django.contrib import admin

from home.models import NavList


@admin.register(NavList)
class NavListAdmin(admin.ModelAdmin):
    pass
