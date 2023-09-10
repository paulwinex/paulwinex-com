from .base import *

DEBUG = False
SECRET_KEY = 'sdfo4ifILF*^E(HFKJSHV*(EFY$#IfnfklEcoieh*&YEVIL'
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = False
ORIGIN = os.getenv('ORIGIN', 'http://localhost:8000')
CORS_ORIGIN_WHITELIST = [ORIGIN]
CSRF_TRUSTED_ORIGINS = [ORIGIN]
CSRF_ALLOWED_ORIGINS = [ORIGIN]
CORS_ORIGINS_WHITELIST = [ORIGIN]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
try:
    from .local import *
except ImportError:
    pass
