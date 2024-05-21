import os
import docker
import nextcord
from nextcord.ext import commands

from datetime import date
import time
import asyncio
import apscheduler
from apscheduler.schedulers.blocking import BlockingScheduler

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

client = commands.Bot(command_prefix='l!', intents=intents, help_command=None, case_insensitive=True)

newtoken = os.environ.get('token', "TOKEN")
Token = newtoken

# Used to send a message to a specific channel
async def send_message(message):
  channel = client.get_channel(1241163646013542582)
  await channel.send(message)

# Used to send a message without input of user
async def send_without_command():
    global send_message
    if True:
        # added auto version
        client = docker.DockerClient(base_url='unix://var/run/docker.sock', version='1.44')
        ctnrNames = client.containers.list(all=True)
        for n in ctnrNames:
            if(client.containers.get(n.name).status != "running"):
                await send_message(n.name + " Down\n")


@client.event
async def on_ready():
    print("Ready")
    await send_without_command()
    print("Sent Message")
    # Check status of docker container and return logs if issue
    
    #scheduler = BlockingScheduler()
    #scheduler.add_job(checkDownContainers, 'interval', hours=int(1))
    #scheduler.start()

extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

client.run(Token)
