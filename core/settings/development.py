from .base import *

EMAIL_HOST = env('DEV_EMAIL_HOST')
EMAIL_HOST_USER = env('DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DEV_EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('DEV_EMAIL_PORT')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
