sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ~/web/ask/
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application&