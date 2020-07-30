# FROM webrecorder/pywb:new-wombat
FROM webrecorder/pywb:2.4.2

WORKDIR /app

COPY config.yaml ./
COPY crawlapp.py ./

COPY uwsgi.ini /uwsgi/

COPY ./templates ./templates
COPY ./static ./static

#WORKDIR /webarchive

