from nextcord import Interaction
import nextcord
import docker
from nextcord.ext import commands
from nextcord.ui import View
from nextcord.ui import Select

class dockerMenu(commands.Cog):
    
    # default initialization
    def __init__(self, client):
        print("DockerMenu Initialized Successfully")
        self.client = client

    @nextcord.slash_command(name="drop",
                        description="Dropdown test")
        
    async def drop(self, interaction:Interaction):

        async def callbackresponse(interaction):
            for values in dropdown.values:
                await interaction.send("You chose option: " + values)

        # Create loop to loop through all the server names
            
        options = []
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        ctnrNames = client.containers.list(all=True)
        for n in ctnrNames:
            options.append(nextcord.SelectOption(label=n.name))
        
        dropdown = Select(placeholder="What docker container would you like to select?", 
                                    options=options,  max_values=1, min_values=1)
            
        dropdown.callback = callbackresponse
        myview = View(timeout=180)
        myview.add_item(dropdown)
        await interaction.send('What docker container would you like to select?', view=myview)
            

# class MenuView(nextcord.ui.View):
#     def __init__(self):
#         super().__init__()
#         self.add_item(Menus())

# class dockerMenu(commands.Cog):
#     def __init__(self, client):
#         print("DockerMenu Initialized Successfully")
#         self.client = client

#     @nextcord.slash_command(name="drop",
#                             description="Dropdown test")
#     async def drop(self, interaction:Interaction):
#         view = MenuView()
#         await interaction.response.send("chose an option", view=view)


def setup(client):
    client.add_cog(dockerMenu(client))