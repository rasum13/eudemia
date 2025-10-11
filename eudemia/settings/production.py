from .base import *

DEBUG = False

ALLOWED_HOSTS = ["rasum.com.np", "media.rasum.com.np", "www.rasum.com.np", ".vercel.app", ".now.sh"]

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
}

MEDIA_URL = "https://media.rasum.com.np/"
MEDIA_ROOT = "/home2/rasumcom/media.rasum.com.np/"
