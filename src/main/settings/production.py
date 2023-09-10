from .base import *

DEBUG = True
SECRET_KEY = 'sdfo4ifILF*^E(HFKJSHV*(EFY$#IfnfklEcoieh*&YEVIL'
ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_ALLOW_ALL = False
# CSRF_TRUSTED_ORIGINS = ['*']
CORS_ORIGIN_WHITELIST = ['http://localhost:8000']
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]
CSRF_ALLOWED_ORIGINS = ["http://localhost:8000"]
CORS_ORIGINS_WHITELIST = ["http://localhost:8000"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
try:
    from .local import *
except ImportError:
    pass
