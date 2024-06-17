#!/bin/bash

cd app

python create_tables.py

python clear_database.py

python triggers.py

python database_entry.py

gunicorn main:application --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000