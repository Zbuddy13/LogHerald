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
        client = docker.from_env()
        ctnrNames = client.containers.list()
        for n in ctnrNames:
            await interaction.send(n.name)
                
def setup(client):
    client.add_cog(Docker(client))