sudo ln -sf /home/box/etc/hello.py  /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart
# sudo gunicorn -w 4 hello:app -b 0.0.0.0:8080
sudo gunicorn -c /home/box/web/etc/hello.py hello:wsgi_application
sudo gunicorn -c /home/box/web/etc/django.py ask.wsgi:application
