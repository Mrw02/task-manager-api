#!/bin/bash
python manage.py migrate --no-input
gunicorn taskapi.wsgi --log-file -
