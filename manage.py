import os
import sys
import sentry_sdk


def main():
    """
    Set up the Django environment and execute command-line instructions.

    This function ensures the DJANGO_SETTINGS_MODULE environment variable
    is set, imports Django's command-line execution function, and passes
    command-line arguments to it.

    Raises:
        ImportError: If Django is not installed or not available in the
            current PYTHONPATH.
    """
    # Set the default Django settings module for the project
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Execute the command-line instruction passed to manage.py
    execute_from_command_line(sys.argv)


# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sentry_sdk.capture_exception(e)  # Envoie l'erreur à Sentry
        raise  # Re-lève l'exception pour voir le traceback dans la console
