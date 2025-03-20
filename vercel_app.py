import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Vercel expects 'handler' as the entry point
handler = get_wsgi_application()
