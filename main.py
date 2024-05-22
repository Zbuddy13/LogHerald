import os
import docker
import nextcord
from nextcord.ext import commands, tasks

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

client = commands.Bot(command_prefix='l!', intents=intents, help_command=None, case_insensitive=True)

Token = os.environ.get('token', "TOKEN")

@client.event
async def on_ready():
    print("Ready")


extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

client.run(Token)
