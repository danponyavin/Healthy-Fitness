#!/bin/bash

python ./database_download.py
python ./healthyfitness/manage.py runserver 0.0.0.0:8000
