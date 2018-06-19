from .base import *
from .settings_secret_prod import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

DEBUG = False

ALLOWED_HOSTS = ['web']

REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': [IsAuthenticatedOrReadOnly],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
