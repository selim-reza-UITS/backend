import os
from .base import *  # noqa: F403
from dotenv import load_dotenv

load_dotenv()
ALLOWED_HOSTS = []

ENV = os.getenv('DJANGO_ENV', 'local')
dotenv_path = BASE_DIR / '.env' / f'.{ENV}' # noqa: F405
load_dotenv(dotenv_path=dotenv_path)

EXTERNAL_APP = [  # noqa: F405
    "corsheaders",
    'rest_framework',
    'rest_framework_simplejwt',
    
]
# installed App
CUSTOM_APP = [
    "coreapi",
    "app.accounts",
]

WSGI_APPLICATION = '_core.wsgi.application'
INSTALLED_APPS = PRIORITY_APP + DEFAULT_APP + EXTERNAL_APP + CUSTOM_APP # noqa: F405

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ENVIRONMENT_NAME = "Production"
ENVIRONMENT_COLOR = "#FF2222"


REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '5/minute',
    }
}