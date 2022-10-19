FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 1337

EXPOSE 1337

RUN pip3 install pycryptodome

COPY ./app/main.py /app
COPY ./app/secp256r1.key /app
COPY ./app/update.log /app
