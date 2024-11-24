from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g+&7x!0r@_3mr44jg%i^k0s^r_j&90ak&9k99execx+bz_&9x+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['alianvari.ir','www.alianvari.ir']

#INSTALLED_APPS = ()

# sites framework
SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE':'mysql.connector.django',
        # 'ENGINE': 'django.db.backends.mysql',
        'NAME': 'alianvariir_travel',
        'USER': 'alianvariir_ali ',
        'PASSWORD': 'Anvari@7768',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_ROOT = '/home/alianvariir/public_html/static'
MEDIA_ROOT ='/home/alianvariir/public_html/media'
# STATICFILES_DIRS = [BASE_DIR/'mysite/statics']


## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

## X-Frame-Options
X_FRAME_OPTIONS = 'SAMEORIGIN'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'