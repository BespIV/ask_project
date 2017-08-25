На 8080 порту приложение hello.py
на 8000 порту ask.wsgi

Чтобы запустить django необходимо из /home/box/web/ask запустить gunicorn: 
gunicorn -b 0.0.0.0:8080 ask.wsgi
