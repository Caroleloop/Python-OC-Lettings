from django.contrib import admin
from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Address model.

    This class customizes how Address instances are displayed in the Django admin site.

    Attributes:
        list_display (tuple): Fields of the Address model to display in the list view.
            - number: Street number of the address.
            - street: Name of the street.
            - city: City of the address.
            - state: State or province.
            - zip_code: Postal code.
            - country_iso_code: ISO country code.
    """

    list_display = ("number", "street", "city", "state", "zip_code", "country_iso_code")


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Letting model.

    This class customizes how Letting instances are displayed in the Django admin site.

    Attributes:
        list_display (tuple): Fields of the Letting model to display in the list view.
            - title: Title of the letting.
            - address: Related Address instance of the letting.
    """

    list_display = ("title", "address")
