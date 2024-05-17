from nextcord import Interaction
import nextcord
from nextcord.ext import commands

class Menus(nextcord.ui.Select):
    
    # default initialization
    def __init__(self):
        print("Callback Initialized Successfully")
        options = [
            nextcord.SelectOption(label="Python", description="python is cool"),
            nextcord.SelectOption(label="Java", description="java is old")
        ]
        async def callbackresponse(interaction:Interaction):
            selected_option = interaction.data.values[0]
            await interaction.response.send_message(f"You chose option: {selected_option}!")

        super().__init__(placeholder="Select your language", min_values=1, max_values=1,options=options)
        callback = callbackresponse()

class MenuView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menus())

class dockerMenu(commands.Cog):
    def __init__(self, client):
        print("DockerMenu Initialized Successfully")
        self.client = client

    @nextcord.slash_command(name="drop",
                            description="Dropdown test")
    async def drop(self, ctx):
        view = MenuView()
        await ctx.send("chose an option", view=view)


def setup(client):
    client.add_cog(dockerMenu(client))