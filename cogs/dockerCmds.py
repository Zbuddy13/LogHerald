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
                
def setup(client):
    client.add_cog(Docker(client))