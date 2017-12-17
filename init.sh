sudo ln -sf /home/box/etc/gunicorn.conf  /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
gunicorn -w 4 hello:app
