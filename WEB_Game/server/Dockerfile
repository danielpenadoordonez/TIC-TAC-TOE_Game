FROM python:3.10-slim-buster

COPY . /api

WORKDIR /api

RUN pip3 install -r requirements.txt && apt-get update && \
apt-get install curl vim -y && pip3 install gunicorn

ENV gunicorn_timeout=200

EXPOSE 8080
 
RUN chmod +x start-api.sh

ENTRYPOINT [ "/bin/bash", "-c", "./start-api.sh" ]   