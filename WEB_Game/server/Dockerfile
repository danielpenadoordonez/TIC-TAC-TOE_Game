FROM python:3.10-slim-buster

COPY . /api

WORKDIR /api

RUN pip3 install -r requirements.txt && apt-get update && \
apt-get install curl vim -y && pip3 install gunicorn

EXPOSE 8080

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8080", "api:tctctoe_server"]