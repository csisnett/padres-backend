from .base import *
from .settings_secret_prod import *

# SECURITY WARNING: keep the secret key used in production secret!


DEBUG = True

ALLOWED_HOSTS = ['web']

REST_FRAMEWORK = {
    
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True
#SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = False
#X_FRAME_OPTIONS = 'DENY'