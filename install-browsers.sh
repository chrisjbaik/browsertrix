#!/bin/sh

# Current Browser
docker pull oldwebtoday/chrome:73
docker pull oldwebtoday/chrome:76

# Base Browser
docker pull oldwebtoday/base-browser

# Borwser automation driver
docker pull webrecorder/autobrowser

if [ "$1" != "--headless" ]; then

    # Required for non-headless mode
    docker pull oldwebtoday/vnc-webrtc-audio
    docker pull oldwebtoday/base-displayaudio
fi

