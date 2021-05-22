import discord
from discord.ext    import commands
import random
import asyncio
import os


bot = commands.Bot(command_prefix='?', description='Use the following commands to mute and unmute everyone in a voice channel.')

@bot.command()
async def dm(ctx):
    """ Mutes everyone in the present voice channel. """
    try:
        #
        member_req = ctx.message.author
        print(member_req)
        # https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.edit
        if (not member_req.dm_channel):
            await member_req.create_dm()
        await member_req.dm_channel.send("Hello %s!" % member_req.name)
    except Exception as errror:
        print('ERROR!!!')
        print(errror)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('READY')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


bot.run('insertbottoken')
