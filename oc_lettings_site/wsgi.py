import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'oc_lettings_site' project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Get the WSGI application callable to serve the project
application = get_wsgi_application()
