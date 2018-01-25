from .project import *


DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prod__db_isound',
        'USER': 'root',
        'PASSWORD': 'aA@299792458*Zz',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
INSTALLED_APPS += []
MIDDLEWARE += []
ALLOWED_HOSTS = [
    'isound.com',
]
# CENTRIFUGO
CENTRIFUGE_ADDRESS = 'https://centrifugo.isound.com/'
CENTRIFUGE_SECRET = ''
