Repo to investigate logging issue with Nginx Unit.
Problem: Nginx unit do not translate python logs to unit.log (unit.log then tranlated to stderr).
Purpose: to see python hosted behind unit with docker logs command.

Steps to reproduce

Pure python startup:
docker build -t python_logging:latest -f python.Dockerfile
docker run --name=python_logging_test -e=PYTHONUNBUFFERED=0-d -p 8080:8080 python_logging:latest
./tests/api_curl.sh
docker stop python_logging_test


Unit with python module startup:
docker build -t unit_python_logging:latest -f unit.Dockerfile
docker run --name=unit_logging_test -e=PYTHONUNBUFFERED=0-d -p 8080:8080 unit_python_logging:latest
./tests/api_curl.sh
docker stop unit_python_logging

Check for logs
docker logs python_logging_test
docker logs unit_python_logging

Expected resul in both cases