#!/bin/bash
docker build --tag=weather_app .
# docker run --network host -v /root/Desktop/Challenges/web/web_weather_app/test:/app/test --rm --name=weather_app -it weather_app
docker run -p 1337:80 -v /root/Desktop/Challenges/web/web_weather_app/test:/app/test --rm --name=weather_app -it weather_app
