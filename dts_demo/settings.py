from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '-f@9yu@b^#-m7j!#x673@zm4&kp80^633pe8#w*#+tm29s(1^m'
SUPERUSER_PASSWORD = os.environ.get('SUPERUSER_PASSWORD')

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0',]

# Application definition
# Apps that are shared across tenants & tenant specific apps are defined here.
SHARED_APPS = (
    'tenant_schemas',# Keep this as high as possible in the list

    'client',# also list the app where the TenantModel resides in

    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'client',
    'cost_resourcing',
    'auth0authorization',
)

INSTALLED_APPS = (
    'tenant_schemas',

    'client',
    'cost_resourcing',
    'auth0authorization',

    'rest_framework',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

DEFAULT_FILE_STORAGE = "tenant_schemas.storage.TenantFileSystemStorage"
TENANT_MODEL = "client.ClientTenancy"

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Added JWT protocol as Authentication option.
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
]

JWT_AUTH = {
    'JWT_PAYLOAD_GET_USERNAME_HANDLER':
        'auth0authorization.utils.jwt_get_username_from_payload_handler',
    'JWT_DECODE_HANDLER':
        'auth0authorization.utils.jwt_decode_token',
    'JWT_ALGORITHM': 'RS256',
    'JWT_AUDIENCE': os.environ.get('JWT_AUDIENCE'),
    'JWT_ISSUER': os.environ.get('JWT_ISSUER'),
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

ROOT_URLCONF = 'dts_demo.urls'

MULTITENANT_TEMPLATE_DIRS = []

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

WSGI_APPLICATION = 'dts_demo.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        "NAME": os.environ.get('DATABASE'),
        "USER": os.environ.get('POSTGRES_USER'),
        "PASSWORD": os.environ.get('POSTGRES_PASSWORD'),
        "HOST": 'db',
        "PORT": '5432',
    }
}

DATABASE_ROUTERS = ['tenant_schemas.routers.TenantSyncRouter',]

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

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
