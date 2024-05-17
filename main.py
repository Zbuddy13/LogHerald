import os
import docker
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

client = commands.Bot(command_prefix='l!', intents=intents, help_command=None, case_insensitive=True)

newtoken = os.environ.get('token', "TOKEN")
Token = newtoken

@client.event
async def on_ready():
    # Check status of docker container and return logs if issue
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    ctnrNames = client.containers.list(all=True)
    for n in ctnrNames:
        if(client.containers.get(n.name).status != "running"):
            print(n.name + "Down\n")


extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

client.run(Token)
