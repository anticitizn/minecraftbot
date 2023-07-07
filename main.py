import asyncio

import discord
from mcstatus import JavaServer

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

server = JavaServer.lookup("kommunique.org")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(mc_status_loop())

async def mc_status_loop():
    while True:
        await get_mc_status()
        await asyncio.sleep(10)  # Wait for 10 seconds

async def get_mc_status():
    try:
        status = server.status()
        print("{0} players online".format(status.players.online))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{0} players online".format(status.players.online)))
    except Exception as e:
        print("An error occurred: ", e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$players'):
        query = server.query()
        if not query.players.names:
            query.players.names.append("No one!")
        await message.channel.send(f"**Players online:** {', '.join(query.players.names)}")

def get_token():
    with open("token.txt", "r") as file:
        return file.read().strip()

client.run(get_token())
