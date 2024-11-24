from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g+&7x!0r@_3mr44jg%i^k0s^r_j&90ak&9k99execx+bz_&9x+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

# sites framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR/'static'
MEDIA_ROOT = BASE_DIR/'media'
STATICFILES_DIRS = [BASE_DIR/'mysite/statics']

X_FRAME_OPTIONS = 'SAMEORIGIN'