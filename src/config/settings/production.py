from .base import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import os

DEBUG = False

ALLOWED_HOSTS = ['web']

REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticatedOrReadOnly'],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',

    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '150/day',
        'user': '1000/day'
    },
}

EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True


SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('RDS_DB_NAME', ''),
        'USER': os.environ.get('RDS_DB_USERNAME', ''),
        'PASSWORD': os.environ.get('RDS_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('RDS_PORT', ''),
    }
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
