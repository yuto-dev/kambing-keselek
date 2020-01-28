from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mbw5p1i()l3wsr#)l697rs(a-c_fm$5x7%*7x_$86s*ix)$z88'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
