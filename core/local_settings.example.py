ALLOWED_HOSTS = ["*"]
DEBUG = True

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "quiz",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
    }
}
