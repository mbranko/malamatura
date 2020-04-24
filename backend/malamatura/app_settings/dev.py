from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ATOMIC_REQUESTS': True,  # opseg transakcije = HTTP zahtev
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fpmh!s6dc3h_^#zuk&(qy6(r1^0!k-q%60b03ki4gg5jpmi1v&'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

API_THROTTLE_RATE = 100
