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

echo "Hello from test static" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

nginx_cong="
server {
	listen 80;
	server_name _;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html;
	}
	location / {
		try_files \$uri \$uri/ =404;
	}
}
"

echo "$nginx_cong" > /etc/nginx/sites-available/default

sudo service nginx restart
