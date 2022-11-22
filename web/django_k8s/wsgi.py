"""
WSGI config for django_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
import os
import pathlib

from django.core.wsgi import get_wsgi_application
from dotenv import read_dotenv

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_k8s.settings")

application = get_wsgi_application()
