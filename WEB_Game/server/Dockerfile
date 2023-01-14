FROM python:3.10-slim-buster

COPY . /tictactoe-server

WORKDIR /tictactoe-server

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "api.py"]