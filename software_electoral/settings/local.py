from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("NAME_SOFTWARE_ELECTORAL_RICHARD"),
        "USER": os.environ.get("USER_SOFTWARE_ELECTORAL_RICHARD"),
        "PASSWORD": os.environ.get("PASSWORD_SOFTWARE_ELECTORAL_RICHARD"),
        "HOST": os.environ.get("HOST_SOFTWARE_ELECTORAL_RICHARD"),
        "PORT": os.environ.get("PORT_SOFTWARE_ELECTORAL_RICHARD"),
        "ATOMIC_REQUEST": True,
    }
}
