FROM python:3.10-slim-buster

COPY . /api

WORKDIR /api

RUN pip3 install -r requirements.txt && apt-get update && \
apt-get install curl vim -y && rm Dockerfile

EXPOSE 8080

CMD ["python3", "api.py"]
