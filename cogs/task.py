import os
import docker
from nextcord.ext import tasks, commands

class task(commands.Cog):
    
    # default initialization
    def __init__(self, client):
        print("Task Initialized Successfully")
        create_dictionary(statusDictionary)
        self.client = client
        self.loop_task.start()

    @tasks.loop(minutes=1.0)
    async def loop_task(self):
        await self.client.wait_until_ready()
        await check_return_status()
        print("Container status checked")

Channel = os.environ.get('channel', "CHANNEL")

# Hold the informaiton of the 
statusDictionary = dict()

# Client for docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# Used to send a message to a specific channel
async def send_message(message):
    channel = client.get_channel(channel)
    await channel.send(message)

# Creates the container names are returns that list
def container_names():
    return client.containers.list(all=True)

# Create dictionary and fill with container names
def create_dictionary(dictionary):
    for n in container_names():
        dictionary[n.name] = client.containers.get(n.name).status

# Used to send a message without input of user
async def check_return_status():
    ctnrStatus = container_names()
    # Iterate through the names in the old dictionary
    for container in statusDictionary:
        # Pull the status of the container
        print("New status" + client.containers.get(container).status)
        print("Old status" + statusDictionary[container])
        if(client.containers.get(container).status != statusDictionary[container]):
            print("Container changed")
            # Set equal to the new status
            statusDictionary[container] = client.containers.get(container).status
            # Send message that the status has changed
            await send_message(container + " Changed\n")

def setup(client):
    client.add_cog(task(client))