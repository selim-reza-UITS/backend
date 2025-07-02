from pathlib import Path
from _core.settings.settings_tweaks.middleware_config import DEFAULT_MIDDLEWARE
from _core.settings.settings_tweaks.template_config import DEFAULT_CONFIG
from _core.settings.settings_tweaks.password_tweaks import DEFAULT_PASSWORD_HASHERS,DEFAULT_PASSWORD_VALIDATOR
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = True
# Application definition
MIDDLEWARE = DEFAULT_MIDDLEWARE
ROOT_URLCONF = '_core.urls'
TEMPLATES = DEFAULT_CONFIG
# Password validation
PASSWORD_HASHERS = DEFAULT_PASSWORD_HASHERS
AUTH_PASSWORD_VALIDATORS = DEFAULT_PASSWORD_VALIDATOR
# 
AUTH_USER_MODEL = "accounts.User"
ADMIN_URL = "dashboard/"