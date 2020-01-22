Repo to investigate logging issue with Nginx Unit.
Problem: Nginx unit do not translate python logs to unit.log (unit.log then tranlated to stderr).
Purpose: to see python hosted behind unit with docker logs command.

Steps to reproduce

Pure python startup:
docker build -f python.Dockerfile -t python_logging:latest .
docker run --name=python_logging_test -e=PYTHONUNBUFFERED=0 -d -p 8080:8080 python_logging:latest
sudo chmod +x ./tests/api_curl.sh
./tests/api_curl.sh
docker stop python_logging_test


Unit with python module startup:
docker build -f unit.Dockerfile -t unit_python_logging:latest .
docker run --name=unit_logging_test -e=PYTHONUNBUFFERED=0 -d -p 8080:8080 unit_python_logging:latest
sudo chmod +x ./tests/api_curl.sh
./tests/api_curl.sh
docker stop unit_python_logging

Check for logs
docker logs python_logging_test
docker logs unit_python_logging

Expected resul in both cases