release: python manage.py migrate --noinput
web: gunicorn --bind :$PORT --workers 4 --worker-class uvicorn.workers.UvicornWorker core.asgi:application
worker: celery -A core worker -P prefork --loglevel=INFO 
beat: celery -A core beat --loglevel=INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
