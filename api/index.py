import os
from django.core.wsgi import get_wsgi_application

# Set default settings module (adjust if your settings file is elsewhere)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Vercel requires a variable named "handler"
handler = get_wsgi_application()
