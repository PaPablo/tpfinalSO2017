#!/bin/bash

echo Starting Gunicorn
ls
exec gunicorn tpfinalso.wsgi --bind 0.0.0.0:80 --reload
