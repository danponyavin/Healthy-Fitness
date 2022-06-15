#!/bin/bash

python ./database_download.py
python ./healthyfitness/manage.py collectstatic
python ./healthyfitness/manage.py makemigrations
python ./healthyfitness/manage.py migrate
python ./healthyfitness/manage.py runserver 0.0.0.0:8000
