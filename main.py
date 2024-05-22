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
Channel = os.environ.get('channel', "CHANNEL")

# Hold the informaiton of the 
statusDictionary = dict()

# Client for docker
client = docker.DockerClient(base_url='unix://var/run/docker.sock')

# Used to send a message to a specific channel
async def send_message(message):
  channel = client.get_channel(channel)
  await channel.send(message)

# Creates the container names are returns that list
async def container_names():
    return client.containers.list(all=True)

# Create dictionary and fill with container names
async def create_dictionary(dictionary):
    for n in container_names():
        dictionary[n.name] = client.containers.get(n.name).status

# Used to send a message without input of user
async def check_return_status():
    global send_message
    ctnrStatus = container_names()
    # Iterate through the names in the old dictionary
    for container in statusDictionary:
        # Pull the status of the container
        if(client.containers.get(container).status != statusDictionary[container]):
            # Set equal to the new status
            statusDictionary[container] = client.containers.get(container).status
            # Send message that the status has changed
            await send_message(container + " Changed\n")

@tasks.loop(minutes=5.0)
async def loop_task():
    check_return_status()
    print("Container status checked")

@client.event
async def on_ready():
    await create_dictionary()
    print("Ready")
    await loop_task()

extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)

client.run(Token)
