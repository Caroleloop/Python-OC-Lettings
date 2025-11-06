import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'oc_lettings_site' project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Get the ASGI application callable to serve the project
application = get_asgi_application()
