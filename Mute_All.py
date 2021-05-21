import discord
from discord.ext    import commands
import random
import asyncio
import os


bot = commands.Bot(command_prefix='?', description='Use the following commands to mute and unmute everyone in a voice channel.')

@bot.command()
async def tm(ctx):
    """ Mutes everyone in the present voice channel. """
    try:
        # https://discordpy.readthedocs.io/en/stable/api.html#voicechannel
        vchan = ctx.message.author.voice.channel
        print(vchan)
        # https://discordpy.readthedocs.io/en/stable/api.html#discord.VoiceChannel.members
        member_list = vchan.members
        print(member_list)
        print('Muting members: ')
        for membr in member_list:
            print(membr.name)
            # https://discordpy.readthedocs.io/en/stable/api.html#discord.Member.edit
            await membr.edit(mute = True)
    except ValueError as errror:
        print('VALUE ERROR FOUND')
        print(errror)
    except AttributeError as NoRror:
        print('VOICE CHANNEL NOT FOUND')
        print(NoRror)


@bot.command()
async def um(ctx):
    """ Unmutes everyone in the present voice channel. """
    try:
        vchan = ctx.message.author.voice.channel
        member_list = vchan.members
        print('Unmuting members: ')
        for membr in member_list:
            print(membr.name)
            await membr.edit(mute = False)
    except ValueError as errror:
        print('VALUE ERROR FOUND')
        print(errror)
    except AttributeError as NoRror:
        print('VOICE CHANNEL NOT FOUND')
        print(NoRror)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print('READY')

@bot.event
async def on_message(message):
    if message.author.top_role.permissions.administrator:
        if message.author == bot.user:
            return
        await bot.process_commands(message)
        
bot.run('INSERT TOKEN HERE')