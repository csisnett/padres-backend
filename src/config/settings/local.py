from .base import *
from .settings_secret_prod import *

# SECURITY WARNING: keep the secret key used in production secret!


DEBUG = True

ALLOWED_HOSTS = ['web', '127.0.0.1']

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



#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True
#SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
#X_FRAME_OPTIONS = 'DENY'