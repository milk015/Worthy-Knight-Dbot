# Discord bot
# feature set:
# Poll system, Music streaming service, auto admin tools
# Author: Jorge Bejarano
# Version: 0.1.0

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
