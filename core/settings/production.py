from .base import *

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')

DATABASES = {
    'default': {
        'ENGINE': env('PS_ENGINE'),
        'NAME': env('PS_NAME'), 
        'USER': env('PS_USER'),
        'PASSWORD': env('PS_PASSWORD'),
        'HOST': env('PS_HOST'), 
        'PORT': env('PS_PORT'),
    }
}
