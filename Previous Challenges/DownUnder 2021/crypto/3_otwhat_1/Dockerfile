FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV LISTEN_PORT 1337

EXPOSE 1337

RUN pip3 install pycryptodome

COPY main.py /app
COPY rsa.key /app
