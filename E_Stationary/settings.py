import os
from pathlib import Path

# Path building inside the project
BASE_DIR = Path(__file__).resolve().parent.parent


# The secret key used in production secret!
SECRET_KEY = 'django-insecure-l_-orv@)j2o5(#97-dnnl2ahtnef*^$2^u547e8zfqt9##6dmd'

#Debug in production
DEBUG = True   

#Allowed Hosts
ALLOWED_HOSTS = ['192.168.0.110']


# All isnatlled application defin
INSTALLED_APPS = [   
    "admin_interface",
    "colorfield", 
    'django.contrib.admin', 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Ink_Spot',
    'storages',
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'E_Stationary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'E_Stationary.wsgi.application'

# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#Passwor validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
MEDIA_URL = '/tcmobilebestrepairserviceforever/'
MEDIA_ROOT = BASE_DIR
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics'),
]



# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Aws access key 
AWS_ACCESS_KEY_ID = "AKIA5TIYTV7MLEWJ3AMZ"
AWS_SECRET_ACCESS_KEY = "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"

AWS_STORAGE_BUCKET_NAME = "mobo-bucket-09"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

ADMIN_MEDIA_PREFIX = f'https://{AWS_S3_CUSTOM_DOMAIN}/admin/'
        
ACCOUNT_SID = "ACb191cb3cbc2ffe0efac329ed3d6ec8af"
AUTH_TOKEN = "8ee010461281a25ff37e2701fda8bef9"