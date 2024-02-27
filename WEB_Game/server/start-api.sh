#/bin/bash


function run(){
    echo "Starting Gunicorn server on 0.0.0.0:8080"
    echo "Gunicorn Timeout: ${gunicorn_timeout}"
    gunicorn -w 1 -b 0.0.0.0:8080 api:tctctoe_server --timeout ${gunicorn_timeout} --log-level debug
}

run
