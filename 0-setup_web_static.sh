#!/usr/bin/env bash
# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
            sudo apt-get update
                sudo apt-get -y install nginx
fi

# Create necessary folders
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo chown -R ubuntu:ubuntu /data/

# Create a fake HTML file
echo "<html><head></head><body>Hello Holberton!</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
config_content="
server {
    listen 80 default_server;
    server_name _;

    location /hbnb_static {

         alias /data/web_static/current/;

         index index.html;
    }

   location /redirect_me {
        return 301 http://www.google.com;
   }

   error_page 404 /404.html;
   location /404 {
        alias /custom_404.html;
        internal;
  }
}"
echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

# Restart Nginx
sudo service nginx restart
