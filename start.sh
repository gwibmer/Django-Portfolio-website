#!/bin/bash
set -e

python manage.py migrate --noinput
python manage.py loaddata home/fixtures/initial_data.json
python manage.py collectstatic --noinput
gunicorn Django_Portfilio_MohammadBurhan.wsgi --log-file -
