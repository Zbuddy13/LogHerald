import docker
client = docker.from_env()
containername = "autohetzner1"
#could add since, and until
ctnrNames = client.containers.list()
selectedContainer = client.containers.get(containername)
print(selectedContainer.logs(timestamps=True))
print(selectedContainer.status)