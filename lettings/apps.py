from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the 'lettings' Django application.

    Attributes:
        default_auto_field (str): Specifies the default type of primary key field
            to use for models in this app. Here, it is set to 'BigAutoField'.
        name (str): Full Python path to the application, used by Django to
            reference this app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "lettings"
