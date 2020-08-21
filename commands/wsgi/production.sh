#!/bin/bash

gunicorn -w $WSGI_WORKERS -b 0.0.0.0:$WSGI_PORT --chdir /srv/project/src settings.wsgi --timeout $WSGI_TIMEOUT
