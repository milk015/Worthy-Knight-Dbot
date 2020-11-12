# Discord bot
# feature set:
# Poll system, Music streaming service, auto admin tools
# Author: Jorge Bejarano
# Version: 0.2.0

import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


# on ready
@bot.event
async def on_ready():
    print("Bot is up and running!")


# Greetings Feature
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.command(name='intro')
async def introduction(res):
    text = "I do stuff I think? the prefix is !...talk to my creator if you want anything."

    response = text
    await res.send(response)


# dice roll
@bot.command(name='dice_toss', alias='dice', help='Rolls a six sided die or dice')
async def roll(res, num_of_dice: int):
    dice = [
        str(random.choice(range(1, 7)))
        for _ in range(num_of_dice)
    ]
    await res.send(', '.join(dice))


# Work in progress
@bot.command(name='poll', help='Makes a poll or vote action')
async def poll_maker(res, num_of_opt: int):
    num = str(num_of_opt)
    ask = "You chose " + num + " options. enter the poll options below"
    await res.send(ask)
    # strings to hold options
    options = ["init"]
    # counter
    counter = 0
    while counter != num_of_opt:
        await res.send(str(counter + 1) + " <--- Enter")
        option_input = await bot.wait_for('message', timeout=60.0)
        print("input capture --> " + str(option_input))
        options.append(option_input.content)
        counter += 1

    print(options)


# audio playback


# dnd game


# quick web search


bot.run(TOKEN)
