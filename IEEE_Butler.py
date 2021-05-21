import discord
from discord.ext import commands
import random
import asyncio
import pickle
import os
import string
import logging

logging.basicConfig(level=logging.INFO)
bot_token = '<INSERT BOT TOKEN HERE>'
randomstartnumber = random.randint(1,100)

######### GLOBAL FUNCTIONS ##########

####### SAVING DATA ########

######################## INITIALIZE BOT #################################
bot = commands.Bot(command_prefix='?', description='test')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

######################### CUSTOM DISCORD COMMANDS #########################
@bot.command()
async def hello(ctx):
    """ Responds \"Hello USERNAME \" """
    await ctx.send("Hello, %s" % (ctx.message.author.display_name))
    
    
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    if (rolls > 20):
        await ctx.send('Too many. Try less.')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
@bot.command()
async def Mroll(ctx, dice: str):
    """Rolls a dice in NdNdN format."""
    try:
        times, rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdNdN!')
        return
    
    for i in range(times):
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

######################### BOT EVENTS #########################
@bot.event
async def on_message(message):
    #srvr_indx = findServerIndex(message.guild.id)
    
    if message.content.startswith('?'):
        pass
    
    await bot.process_commands(message)
    

path = os.path.dirname(os.path.abspath(__file__))
print('Running on:', path)

bot.run(bot_token)


