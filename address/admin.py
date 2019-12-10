from django.contrib import admin

from address.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
