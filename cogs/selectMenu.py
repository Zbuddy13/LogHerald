from nextcord import Interaction
import nextcord
import docker
from nextcord.ext import commands, tasks
from nextcord.ui import View
from nextcord.ui import Select

class dockerMenu(commands.Cog):
    
    # default initialization
    def __init__(self, client):
        print("DockerLogDropdown Initialized Successfully")
        self.client = client

    @nextcord.slash_command(name="dkrlogs",
                        description="Dropdown test")
        
    async def dkrlogs(self, interaction:Interaction, lines: int = 0):

        # Called after user selects an option from the drop down
        async def callbackresponse(interaction):
            print("Callback Initiated")
            client = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto')
            ctnrNames = client.containers.list(all=True)
            embed = nextcord.Embed(title="Log Results")
            # add streaming option for logs
            for values in dropdown.values:
                # Remove the logstr begining and ending format
                # might need loop to remove newline
                logstr = client.containers.get(values).logs(timestamps=True, tail=lines)
                embed.add_field(name="", value=logstr.decode())
                
            await interaction.send(embed=embed)

        # Add all the docker containers to a array then print them out    
        options = []
        client = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto')
        ctnrNames = client.containers.list(all=True)
        for n in ctnrNames:
            options.append(nextcord.SelectOption(label=n.name))
        
        dropdown = Select(placeholder="Containers", 
                                    options=options,  max_values=1, min_values=1)
            
        dropdown.callback = callbackresponse
        myview = View(timeout=180)
        myview.add_item(dropdown)
        await interaction.send('What docker container would you like to select?', view=myview)
            
@tasks.loop(minutes=5.0)
async def loop_task():
    check_return_status()
    print("Container status checked")

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