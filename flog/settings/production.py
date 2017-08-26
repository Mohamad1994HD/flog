import os

try:
    import secretkey
except:
    pass
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.environ.get('SECRET_KEY') or secretkey.SECRET_KEY

DEBUG = False

ALLOWED_HOSTS = ['www.foodbelieve.faith']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # 3rd party
    'tagging',
    'crispy_forms',
    'django_summernote',
    'hitcount',
    # custom apps
    'posts',
    'accounts',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'flog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'flog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/' # origin of permanent static files
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn") # temporarly loc

MEDIA_URL = "/media/"
MEDIA_ROOT = '/home/mohdhd1994/projects/foodblog/flog/media' #os.path.join(os.path.dirname(BASE_DIR), "media")


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]


# TAGGING SYSTEM SETTINGS
FORCE_LOWERCASE_TAGS = False
MAX_TAG_LENGTH = 50

# VIEW SETTINGS
INDEX_MAIN_MAX = 6 
INDEX_ARCHIEVE_MAX = 6
INDEX_TIP_MAX = 6

# SUMMERNOTE CONFIG
SUMMERNOTE_CONFIG = {
    'width': '100%',
    'height': '800',

    'toolbar': [
        ['style', ['style']],
        ['fontstyle', ['bold', 'italic', 'underline', 'clear', 'fontsize']],
        ['fontname', ['fontname']],
        ['color', ['color']],
        ['para', ['ul', 'ol', 'height']],
        ['insert', ['table', 'link', 'picture', 'hr']],
    ], 
    #'attachement_upload_to': utils.upload_location,
}

#EMAIL

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('NOREPLY_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('NOREPLY_EMAIL_PASS')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get('NOREPLY_EMAIL_DEFAULT')


# SOCIAL
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('FACEBOOK_AUTH_KEY')  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_AUTH_SECRET') # App Secret
SOCIAL_AUTH_URL_NAMESPACE = 'accounts:social'
LOGIN_URL = 'accounts:login'
LOGOUT_URL = 'accounts:logout'
LOGIN_REDIRECT_URL = 'posts:index'
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
# extension
    'accounts.pipelines.grab_profile_pic',
#
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
