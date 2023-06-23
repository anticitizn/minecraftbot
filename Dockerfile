FROM python:3.10-bullseye
RUN pip install --upgrade pip
WORKDIR ./
COPY . ./
RUN pip install discord.py
RUN python3 -m pip install 'mcstatus @ git+https://github.com/py-mine/mcstatus@master'