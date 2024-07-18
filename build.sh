#!/bin/bash

# Update package list and install PortAudio
apt-get update && apt-get install -y portaudio19-dev

# Make sure any further commands in the build process continue to run
exec "$@"
