import os
import docker
from nextcord.ext import tasks, commands

class task(commands.Cog):
    
    # default initialization
    def __init__(self, client):
        print("Task Initialized Successfully")
        self.client = client
        self.loop_task.start()

    Channel = os.environ.get('channel', "CHANNEL")

    # Hold the informaiton of the 
    statusDictionary = dict()

    # Client for docker
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')

    # Used to send a message to a specific channel
    async def send_message(message):
        global client
        channel = client.get_channel(channel)
        await channel.send(message)

    # Creates the container names are returns that list
    async def container_names():
        return client.containers.list(all=True)

    # Create dictionary and fill with container names
    async def create_dictionary(dictionary):
        global container_names
        for n in container_names():
            dictionary[n.name] = client.containers.get(n.name).status

    # Used to send a message without input of user
    async def check_return_status():
        global send_message
        global statusDictionary
        ctnrStatus = container_names()
        # Iterate through the names in the old dictionary
        for container in statusDictionary:
            # Pull the status of the container
            if(client.containers.get(container).status != statusDictionary[container]):
                # Set equal to the new status
                statusDictionary[container] = client.containers.get(container).status
                # Send message that the status has changed
                await send_message(container + " Changed\n")

    @tasks.loop(minutes=1.0)
    async def loop_task(self):
        global check_return_status
        await self.client.wait_until_ready()
        check_return_status()
        print("Container status checked")

def setup(client):
    client.add_cog(task(client))