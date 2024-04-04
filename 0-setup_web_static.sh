#!/usr/bin/env bash
#set up a web server for the deployment of web_static

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
ln -sf  /data/web_static/releases/test/ 
sudo chown -R "ubuntu":"ubuntu" /data/ /data/web_static/current

sed -i "48i \\\tlocation /hbnb_static \{\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t\}" /etc/nginx/sites-available/default
sudo nginx -t
sudo service nginx restart
