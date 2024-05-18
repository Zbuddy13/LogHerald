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

Token = ""

async def send_message(message):
  channel = client.get_channel(1241163646013542582)
  await channel.send(message)

async def send_without_command():
    global send_message
    if True:
        await send_message("Down working")

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
