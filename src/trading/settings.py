"""
Django settings for trading project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h44n-^i48tjjo85glfd!-@nb9%+1#2^ll3kbvnadzi=08(fkny'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '6a084482f895.ngrok.io', # für ngrok
    '127.0.0.1' 
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    


    #third party apps
    'bokeh', # Für die Generierung von Graphen
    'pandas', # Abhängigkeit von bokeh
    'jsonfield',
    'ckeditor', # Für Code Highlighter als TextEditor
    'ckeditor_uploader' , # Für Code Highlighter als TextEditor
    

    # eigene Apps
    'account',
    'regel',
    'indikator',
    'strategie',
    'simulation',
]

# CKEDITOR Einstellung, ermöglicht code-snippets mit highlighting
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS={
    'default': {
        'toolbar': 'Custom',
        'height': 500,
        'toolbar_Custom':[
            ['Bold','Link','Image'],
        ],
    },
    'special': 
    {'toolbar': 'Special', 'height': 500,
        'toolbar_Special': 
            [
                ['CodeSnippet'], # here
            ], 
            'extraPlugins': 'codesnippet', # here
            'codeSnippet_languages': {
		        'javascript': 'JavaScript',
		        'python': 'Python'
	        }
        }
        
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #Custom Middleware
    'trading.auth_middleware.AngemeldetMiddleware',
    
]

ROOT_URLCONF = 'trading.urls'

CORS_ORIGIN_ALLOW_ALL = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

AUTH_USER_MODEL = 'account.Account'

WSGI_APPLICATION = 'trading.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [ # Djangos Passwort  Validierung deaktiviert und mit eigenem Validierer ersteztz
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
    {   
        'NAME': 'account.validation.CustomPasswordValidator', # eigener Validierer
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

DATE_FORMAT = "%Y-%m-%d"

TIME_ZONE = 'Europe/London'


USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'root')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static/bootstrap'),
]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

#Wichtig für die Middleware
AUTH_EXEMPT_ROUTES = ('registrieren','login','about') #Seiten die nicht betroffen sind von der Weiterleitung
AUTH_LOGIN_ROUTE = 'login-view' #Seite auf die Weitergeleitet werden soll

BACKEND_URL = "http://8fd0b6278897.eu.ngrok.io/" # Hier kommt die URL der API des Backends