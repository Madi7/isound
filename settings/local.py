from .base import *


DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_isound',
        'USER': 'root',
        'PASSWORD': '299792458',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
INSTALLED_APPS += [
    'debug_toolbar',
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]
# CENTRIFUGO
CENTRIFUGE_ADDRESS = 'http://localhost:8077'
CENTRIFUGE_SECRET = ''

# DEBUG-TOOLBAR
INTERNAL_IPS = (
    '127.0.0.1',
    'localhost',
)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_PATCH_SETTINGS = False
