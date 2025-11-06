from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing a physical address.

    Attributes:
        number (PositiveIntegerField): Street number (max value 9999).
        street (CharField): Street name (max length 64).
        city (CharField): City name (max length 64).
        state (CharField): State abbreviation (exactly 2 characters).
        zip_code (PositiveIntegerField): Postal code (max value 99999).
        country_iso_code (CharField): ISO country code (exactly 3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Return a human-readable string representation of the Address.

        Returns:
            str: The street number and street name (e.g., "123 Main St").
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Meta options for the Address model.
        """

        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model representing a letting (rental property).

    Attributes:
        title (CharField): Title of the letting (max length 256).
        address (OneToOneField): One-to-one relationship with an Address.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a human-readable string representation of the Letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
