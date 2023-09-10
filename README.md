### paulwinex.com

My personal site project.

_Based on Wagtail_

## Install

```shell
git clone https://github.com/paulwinex/paulwinex-com.git
cd paulwinex.com
```
Create `.env` file

Change values if needed.

```shell
tee -a .env << END
APP_NAME=pw
APP_PORT=8080
DATA_DIR=./data
ORIGIN=https://mydomain.com
END
```

## Build the image

```shell
docker-compose build
docker-compose up -d
```

## Init app

```shell
docker exec pw-app ./manage.py migrate
docker exec pw-app ./manage.py collectstatic --noinput
docker exec -it pw-app ./manage.py createsuperuser
```

## Setup Nginx

Edit config `configs/app.nginx`. Change paths to data dir

Link config

```shell
ln -s ./configs/app.nginx /etc/nginx/sites-enabled/app.nginx
```
Check

```shell
sudo nginx -t
```

Reload Nginx

```shell
sudo nginx -s reload
```

## Create certificates

```shell
apt install -y nginx certbot python3-certbot-nginx
```

Create certificates

```shell
certbot
```

