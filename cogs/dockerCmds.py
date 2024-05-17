import docker
import nextcord
from nextcord.ext import commands
from nextcord import Interaction

# Docker cog used to interact with a docker container
class Docker(commands.Cog):

    # default initialization
    def __init__(self, client):
        print("Docker Initialized Successfully")
        self.client = client

    @nextcord.slash_command(name="names",
                            description="View a list of docker container names")
    
    async def names(self, interaction: Interaction):
        # Grab the default client
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        ctnrNames = client.containers.list()
        allContainers = ""
        for n in ctnrNames:
            allContainers = allContainers + n.name + '\n'
            
        await interaction.send(allContainers)

    @nextcord.slash_command(name="logs",
                            description="View the logs for a container")
    
    async def logs(self, interaction: Interaction, containername: str = ' '):
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        #could add since, and until
        ctnrNames = client.containers.list()
        selectedContainer = client.containers.get(containername)
        await interaction.send(selectedContainer.logs(timestamps=True))

    @nextcord.slash_command(name="status",
                            description="View the status of a selected container")
    
    async def status(self, interaction: Interaction, containername: str = ' '):
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        ctnrNames = client.containers.list()
        selectedContainer = client.containers.get(containername)
        await interaction.send(selectedContainer.status)
                
def setup(client):
    client.add_cog(Docker(client))