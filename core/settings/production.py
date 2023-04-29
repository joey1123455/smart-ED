from .base import *

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
