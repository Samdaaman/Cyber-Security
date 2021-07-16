#!/bin/bash
docker rm -f web_caas
docker build -t web_caas . && \
docker run --name=web_caas --rm --network host -it web_caas