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
@bot.command(name='poll', help = 'Makes a poll or vote action. Up to 4 options!(even if you enter more than 4)')
async def poll_maker(res, num_of_opt: int):
    # setting limit and ending func if lower than 0
    if num_of_opt > 4:
        num_of_opt = 4
    elif num_of_opt < 0:
        return await res.send("Enter a number higher than 0 next time....")
    # function start
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
    # string clean up, removing init, creating string to print
    options.pop(0)
    text_counter = 0
    vote_text = "Your choices are: "
    while text_counter != num_of_opt:
        if text_counter == num_of_opt - 1:
            vote_text = vote_text + str(text_counter + 1) + ". " + str(options[text_counter])
        else:
            vote_text = vote_text + str(text_counter + 1) + ". " + str(options[text_counter]) + ", "
        text_counter += 1
    # printing poll options
    await res.send("you have 60 seconds to vote!!! react with the number you want!!")
    await res.send(vote_text)

    # accepting votes
    # reactions to capture :one:, :two:, :three:, :four:

    reactions = [':one:', ':two:', ':three:', ':four']


# audio playback


# dnd game


# quick web search


bot.run(TOKEN)
