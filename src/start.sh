#!/bin/bash

gunicorn --workers=2 \
         --env DJANGO_SETTINGS_MODULE=main.settings.production \
         --bind 0.0.0.0:8080 \
         main.wsgi
