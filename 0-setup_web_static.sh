#!/usr/bin/env bash
#sets up the web servers for the deployment of web_static.

sudo apt update
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R "ubuntu":"ubuntu" /data/

sudo sed -i '45 i\\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;  \n\t\t\}' /etc/nginx/sites-available/default
sudo service nginx restart
