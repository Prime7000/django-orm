DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

INSTALLED_APPS = [
    "myapp",  # register your app so makemigrations works
]

SECRET_KEY = "dummy-key"   # needed by Django
