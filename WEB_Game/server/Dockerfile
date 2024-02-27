FROM python:3.10-slim-buster

COPY . /api

WORKDIR /api

RUN pip3 install -r requirements.txt && apt-get update && \
apt-get install curl vim -y && pip3 install gunicorn

ENV gunicorn_timeout=200

EXPOSE 8080
 
#CMD ["sh", "-c", "gunicorn", "-w 1", "-b", "0.0.0.0:8080", "api:tctctoe_server", "--timeout", "$gunicorn_timeout", "--log-level", "debug"]
RUN chmod +x start-api.sh

ENTRYPOINT [ "/bin/bash", "-c", "./start-api.sh" ]   