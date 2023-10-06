#!/usr/bin/env bash
#This Bash script sets up web servers for the deployment of the web static

if ! command -v nginx &>/dev/null;
then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

echo "Hello World!" | sudo tee /var/www/html/index.html

REDIRECTION=$(cat << EOF

	add_header X-Served-By $(hostname);

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	location /hbnb_static/ {
		alias /data/web_static/current/;
		index index.html;
	}

	error_page 404 /custom_404.html;

	location /custom_404.html {
		root /var/www/html;
	}
EOF
)

sudo sed -i '/^server {/r /dev/stdin' /etc/nginx/sites-enabled/default <<< "$REDIRECTION"

echo "Ceci n'est pas une page" | sudo tee /var/www/html/custom_404.html

sudo service nginx restart
