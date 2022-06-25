"""
Django settings for nakhll project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import sentry_sdk
import os
import logging
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from datetime import timedelta
from dotenv import load_dotenv
from django.urls.base import reverse_lazy

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGIN = '/profile/'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/profile/'
LOGOUT_REDIRECT_URL = '/'
REDIRECT_FIELD_NAME = 'next'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = int(os.environ.get("DEBUG", default=0))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

COMPRESS_ENABLED = True

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'analytical',
    'tinymce',
    'admin_reorder',
    'django_jalali',
    'simple_history',
    'oauth2_provider',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'imagekit',
    'compressor',
    'mathfilters',
    'django_prometheus',
    'django_extensions',
    'colorfield',
    'django_rename_app',
    'drf_yasg',
    'import_export',
]

NAKHLL_APPS = [
    'nakhll_auth',
    'nakhll_market',
    'restapi',
    'cart',
    'coupon',
    'logistic',
    'invoice',
    'accounting',
    'payoff',
    'torob_api',
    'url_redirector',
    'custom_list',
    'shop',
    'sms',
    'reports',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + NAKHLL_APPS

MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ADMIN_REORDER = (
    {'app': 'nakhll_market', 'models': (
        'nakhll_market.Pages',
        'nakhll_market.Profile',
        'nakhll_market.Market',
        'nakhll_market.SubMarket',
        'nakhll_market.Shop',
        'nakhll_market.Product',
        'nakhll_market.ProductBanner',
        'nakhll_market.Category',
        'nakhll_market.Tag',
        'nakhll_market.ProductTag',
        'nakhll_market.Attribute',
        'nakhll_market.AttrPrice',
        'nakhll_market.Comment',
        'nakhll_market.Review',
        'nakhll_market.Message',
        'nakhll_market.Survey',
        'nakhll_market.Slider',
        'nakhll_market.Option_Meta',
        'nakhll_market.Alert',
        'nakhll_market.AmazingProduct',
        'nakhll_market.LandingPageSchema',
        'nakhll_market.ShopPageSchema',
        'shop.ShopFeature',
        'nakhll_market.LandingPage',
        'nakhll_market.LandingImage',
        'coupon.Coupon',
    )},
    {
        'app': 'logistic',
        'models': (
            'logistic.Address',
            'logistic.LogisticUnitGeneralSetting',
            'logistic.ShopLogisticUnit',
            'logistic.ShopLogisticUnitConstraint',
            'logistic.ShopLogisticUnitCalculationMetric',
        )
    },
    {'app': 'payoff', 'label': 'بخش مالی جدید', 'models': (
        'payoff.Transaction',
        'payoff.TransactionResult',
        'payoff.TransactionReverse',
        'payoff.TransactionConfirmation',
    )},
    {'app': 'invoice', 'label': 'بخش حسابداری جدید', 'models': (
        'invoice.Invoice',
        'invoice.InvoiceItem',
        'shop.ShopFeature',
        'shop.ShopFeatureInvoice',
        'shop.ShopLanding',
    )},
    {'app': 'Ticketing', 'label': 'بخش پشتیبانی و گزارشات', 'models': (
        'Ticketing.Ticketing',
    )},
    {'app': 'auth', 'label': 'کاربران و دسترسی ها'},
    {'app': 'sites', 'label': 'دسترسی SiteMap'},
    {'app': 'url_redirector', 'label': 'تغییر دهنده Url'},

    # repost panel
    {'app': 'reports', 'label': 'گزارشات'},

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'nakhll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'nakhll.wsgi.application'
IMAGEKIT_CACHEFILE_DIR = 'media/CACHE/images'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


PERSISTENT_STORAGE = "/mnt/shared-volume"

DATABASES = {
    # "mysql": {
    #     "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.mysql"),
    #     "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
    #     "USER": os.environ.get("SQL_USER", "user"),
    #     "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
    #     "HOST": os.environ.get("SQL_HOST", "localhost"),
    #     "PORT": os.environ.get("SQL_PORT", "3306"),
    #     'OPTIONS': {
    #         # Tell MySQLdb to connect with 'utf8mb4' character set
    #         'charset': 'utf8mb4',
    #     },
    #     'CONN_MAX_AGE': None,
    # },
    'default': {
        'ENGINE': os.environ.get('POSTGRES_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('POSTGRES_DB', 'nakhlldb'),
        'USER': os.environ.get('POSTGRES_USER', 'nakhll'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '12345'),
        'HOST': os.environ.get('POSTGRES_HOST', 'postgres'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static-django/'

MEDIA_ROOT = os.path.join(BASE_DIR, '')
MEDIA_URL = '/'

SESSION_COOKIE_AGE = 216000

CART_SESSION_ID = 'cart'

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'},
    'OAUTH_BACKEND_CLASS': 'oauth2_provider.oauth2_backends.JSONOAuthLibCore',
    'ACCESS_TOKEN_EXPIRE_SECONDS': 86400,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'EXCEPTION_HANDLER': 'nakhll.utils.custom_exception_handler'
}
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.environ.get(
        'ACCESS_TOKEN_EXPIRE_MINUTES',
        5))  # 5 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = int(
    os.environ.get(
        'REFRESH_TOKEN_EXPIRE_MINUTES',
        1440))  # 24 hours
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

SITE_ID = os.environ.get('SITE_ID', 2)

# admin users that detail trace back of unhandelled exception are sent to them.
ADMINS = [tuple(os.environ.get('ADMINS', '').split())]
SERVER_EMAIL = os.environ.get('EMAIL_HOST_USER')

# setup email configurations
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = bool(os.environ.get('EMAIL_USE_TLS'))
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 587)

sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)

# setup sentry
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DNS"),
    integrations=[
        DjangoIntegration(),
        sentry_logging,
    ],
    traces_sample_rate=1.0,
    environment=os.environ.get("SENTRY_ENVIRONMENT", "production"),
    send_default_pii=True,
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

KAVENEGAR_KEY = os.environ.get('KAVENEGAR_KEY')

SESSION_SAVE_EVERY_REQUEST: bool = True

# analytical
GOOGLE_ANALYTICS_SITE_SPEED = True

ANALYTICAL_AUTO_IDENTIFY = True

GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-189302977-1'
GOOGLE_ANALYTICS_GTAG_PROPERTY_ID = 'UA-189302977-1'
GOOGLE_ANALYTICS_JS_PROPERTY_ID = 'UA-189302977-1'


def IDENTITY_FUNCTION(user): return user.id


SENDSMS_BACKEND = 'sms.backend.SmsBackend'
HOTJAR_SITE_ID = '2447146'

# CORS Settings
CORS_ORIGIN_ALLOW_ALL = bool(os.environ.get('CORS_ALLOW_ALL_ORIGINS'))
CORS_ALLOW_CREDENTIALS = bool(os.environ.get('CORS_ALLOW_CREDENTIALS', True))
if not CORS_ORIGIN_ALLOW_ALL:
    CORS_ORIGIN_WHITELIST = os.environ.get(
        'CORS_ORIGIN_WHITELIST',
        'http://localhost:3007').split(' ')
CORS_ALLOW_HEADERS = os.environ.get(
    'CORS_ALLOW_HEADERS', 'accept accept-encoding authorization content-type origin\
                         dnt user-agent x-csrftoken x-requested-with').split(' ')
CORS_ALLOW_METHODS = os.environ.get(
    'CORS_ALLOW_METHODS',
    'DELETE GET OPTIONS PATCH POST PUT').split(' ')

DOMAIN_NAME = os.environ.get('DOMAIN_NAME', 'https://nakhll.com')

INVOICE_EXPIRING_HOURS = 4

DISCORD_WEBHOOKS = {
    'ALERT': os.environ.get('DISCORD_ALERT_WEBHOOK'),
    'PURCHASE': os.environ.get('DISCORD_PURCHASE_WEBHOOK'),
    'NEW_PRODUCT': os.environ.get('DISCORD_NEW_PRODUCT_WEBHOOK'),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[DJANGO] %(levelname)s %(asctime)s %(module)s '
                      '%(name)s.%(funcName)s:%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        }
    },
    'loggers': {
        '*': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

# django-debug-toolbar settings
if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
