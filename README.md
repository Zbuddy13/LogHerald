# LogHerald Bot
A Discord bot for monitoring the status of various docker containers

An example compose is ->
```
services:
    logherald:
        container_name: logheraldProto
        privileged: true
        environment:
            - token='insert your token here'
        volumes:
            - /mnt/appdata/logHerald/data:/data
            - /var/run:/var/run # For access to docker sock
        restart: always
        image: zbuddy19/logherald:latest
```
