from nextcord import Interaction
import nextcord
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
            
        options = [
            nextcord.SelectOption(label="Python", description="python is cool"),
            nextcord.SelectOption(label="Java", description="java is old")
        ]

        dropdown = Select(placeholder="What docker container would you like to select?", 
                                    options=options,  max_values=1, min_values=1)
            
        dropdown.callback = callbackresponse
        myview = View(timeout=180)
        myview.add_item(dropdown)
        await interaction.send('Hello!', view=myview)
            

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