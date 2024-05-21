FROM python:3.11.2-alpine
#FROM --platform=linux/arm python:3.10.11-alpine3.17 as build

# Adding Labels to identify repository for github
LABEL AUTHOR="ZBUDDY"
LABEL org.opencontainers.image.source=https://github.com/Zbuddy13/LogHerald
LABEL org.opencontainers.image.description="Containerized Version of logHerald"
LABEL org.opencontainers.image.licenses=MIT

# upgrade pip and install requirements.
COPY /requirements.txt /requirements.txt
RUN pip3 install --upgrade pip3
RUN pip3 install -r /requirements.txt
RUN apk update
RUN apk upgrade --available && sync

# Set work directory, copy source code to there
WORKDIR /app
COPY . .

# Set Arguments
ENV token="TOKEN"

CMD [ "python3", "-u", "main.py" ]