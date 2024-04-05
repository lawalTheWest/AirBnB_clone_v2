#!/usr/bin/env bash
# This bash script configures Nginx server
# with some folders and files
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
# Create the folder:
# 	/data/web_static/
#	/data/web_static/releases/
#	/data/web_static/shared/
#	/data/web_static/releases/test/
#	
# if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a fake html file:
#	/data/web_static/releases/test/index.html
echo "Testing the Nginx configuration" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
conf="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "45i $conf" /etc/nginx/sites-available/default
sudo service nginx start
sudo service nginx restart
sudo service nginx reload
