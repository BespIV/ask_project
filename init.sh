sudo cp /home/box/web/etc/nginx.conf /etc/nginx/sites-available/nginx.conf
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/nginx.conf
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
