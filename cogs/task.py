import os
import docker
import nextcord
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
        msgchannel = self.client.get_channel(messageChannel)
        await check_return_status(msgchannel)
        print("Container status checked")

messageChannel = os.environ.get('channel', "CHANNEL")

# Hold the informaiton of the 
statusDictionary = dict()

# Client for docker
dkrclient = docker.DockerClient(base_url='unix://var/run/docker.sock')

# Creates the container names are returns that list
def container_names():
    return client.containers.list(all=True)

# Create dictionary and fill with container names
def create_dictionary(dictionary):
    for n in container_names():
        dictionary[n.name] = dkrclient.containers.get(n.name).status

# Used to send a message without input of user
async def check_return_status(channel):
    # Iterate through the names in the old dictionary
    for container in statusDictionary:
        # Pull the status of the container
        print("New status" + dkrclient.containers.get(container).status)
        print("Old status" + statusDictionary[container])
        if(dkrclient.containers.get(container).status != statusDictionary[container]):
            print("Container changed")
            # Set equal to the new status
            statusDictionary[container] = dkrclient.containers.get(container).status
            # Send message that the status has changed
            await channel.send(container + " Changed\n")

def setup(client):
    client.add_cog(task(client))