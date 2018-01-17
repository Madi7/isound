import os
import sys
from . import secret


SECRET_KEY = secret.SECRET_KEY
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_isound',
        'USER': secret.DB_USER,
        'PASSWORD': secret.DB_PASSWORD,
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    #'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'debug_toolbar',
    'music.apps.MusicConfig'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]
ADMINS = [
    ('Madi', 'madi7maratovic@gmail.com')
]
CSRF_COOKIE_SECURE = False

# PATH - Project-Directory
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(PROJECT_DIR)

# PATH - Apps
sys.path.append(os.path.join(PROJECT_DIR, 'apps'))

# PATH - Urls
ROOT_URLCONF = 'urls.urls'

# PATH - Static
STATIC_URL = '/static/'

# PATH - Media
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

# PATH - WSGI
WSGI_APPLICATION = 'isound.wsgi.application'

# Develop = True | Production = False
DEBUG = True

# Shell+ Custom Imports
SHELL_PLUS = 'plain'
SHELL_PLUS_PRE_IMPORTS = [
    ('django.db.models', ('Avg', 'Count', 'Max', 'Min', 'F', 'Q', 'ExpressionWrapper', 'Case', 'Value', 'When', 'IntegerField', 'CharField', 'fields')),
    ('django.contrib.auth.models', 'User'),
    ('music.models', ('Album', 'Song')),
]
# REST_FrameWork & JSON-Web-Token-Auth
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
# Localization
LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# OTHER
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
