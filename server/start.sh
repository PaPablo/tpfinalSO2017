#!/bin/bash

echo Starting Gunicorn
exec gunicorn tpfinalso.wsgi --bind 0.0.0.0:80
