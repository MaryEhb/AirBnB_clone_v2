#!/usr/bin/env bash
# Bash script that sets up your web servers for
#the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

nginx_cong="
server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location /redirect_me {
                return 301 https://github.com/MaryEhb;
        }
        location /hbnb_static {
                alias /data/web_static/current;
                index index.html;
        }
        error_page 404 /404.html;
        location = /404.html {
                internal;
        }
}
"

echo "$nginx_cong" > /etc/nginx/sites-available/default
echo "$nginx_cong" > /etc/nginx/sites-enabled/default

sudo service nginx restart
