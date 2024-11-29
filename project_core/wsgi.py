"""
WSGI config for project_core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_core.settings')

application = get_wsgi_application()

# Declarar la variable 'app' como 'application' para que se utilice como punto de entrada para vercel.
app = application