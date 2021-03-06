from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u+*x1yntp)c7e6cd8532(-3gmyb0!891!2&p4=x416@rpw0j_k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'crispy_forms',
    "crispy_tailwind",
    'tailwind',
    "theme",
    'django_browser_reload',

    # Local apps
    'leads',
    'agents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'djcrm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates" ],
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

WSGI_APPLICATION = 'djcrm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'djcrm',
        'USER': 'postgres',
        'PASSWORD':'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = "static_root"
MEDIA_URL = "/media/"
MEDIA_ROOT = "media_root"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'leads.User'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LOGIN_REDIRECT_URL = '/leads'
LOGIN_URL = '/login'
LOGOUT_REDIRECT_URL = "/"
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = 'tailwind'

#if not DEBUG:
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    #SECURE_SSL_REDIRECT = True
    #SESSION_COOKIE_SECURE = True
    #CSRF_COOKIE_SECURE = True
    #SECURE_BROWSER_XSS_FILTER = True
    #SECURE_CONTENT_TYPE_NOSNIFF = True
    #SECURE_HSTS_SECONDS = 31536000  # 1 year
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    #SECURE_HSTS_PRELOAD = True
    #X_FRAME_OPTIONS = "DENY"

    #ALLOWED_HOSTS = ["*"]

    #EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    #EMAIL_HOST = env("EMAIL_HOST")
    #EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    #EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    #EMAIL_USE_TLS = True
    #EMAIL_PORT = env("EMAIL_PORT")
    #DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

TAILWIND_APP_NAME = 'theme'

NPM_BIN_PATH = r"C:\Users\Admin\Envs\test\npm.cmd"