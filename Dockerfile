FROM python:3.10-bullseye
RUN pip install --upgrade pip
WORKDIR ./
COPY . ./
RUN pip install -r requirements.txt