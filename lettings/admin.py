from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("number", "street", "city", "state", "zip_code", "country_iso_code")


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = ("title", "address")
