#!/usr/bin/env bash

# Sets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
nginx_config="
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	server_name _;
	add_header X-Served-By \$HOSTNAME;

	location /hbnb_static/ {
		alias /data/web_static/current/;
		index index.html;
	}
}"

echo "$nginx_config" | sudo tee /etc/nginx/sites-enabled/default >/dev/null

# Restart Nginx
sudo service nginx restart
