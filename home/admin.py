from django.contrib import admin

from home.models import NavList, Panel, PanelContents


@admin.register(NavList)
class NavListAdmin(admin.ModelAdmin):
    pass


@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    pass


@admin.register(PanelContents)
class PanelContentsAdmin(admin.ModelAdmin):
    pass
