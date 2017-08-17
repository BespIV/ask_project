Запустить gunicorn' ом приложение hello.py:

sudo gunicorn -b 0.0.0.0:8080 hello:app