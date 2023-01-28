# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /homepage

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple

COPY . .

CMD ["python3", "run_http.py"]