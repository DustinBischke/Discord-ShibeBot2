import asyncio
import config
import discord
import os
from discord.ext.commands import Bot, when_mentioned_or

bot = Bot(command_prefix = when_mentioned_or(config.prefix),
          description = config.description,
          case_insensitive=True,
          activity=discord.Game(config.game))

@bot.event
async def on_ready():
    print('Connected as: {}'.format(bot.user.name))
    print('Discord.py Version: {}'.format(discord.__version__))

    cogs = os.listdir('cogs')

    if '__pycache__' in cogs:
        cogs.remove('__pycache__')

    for cog in cogs:
        bot.load_extension('cogs.{}'.format(cog.replace('.py', '')))
        print('Loaded extension: ' + cog)

@bot.event
async def on_server_join(server):
    print('Added to server: {}'.format(server.name))

@bot.event
async def on_server_leave(server):
    print('Removed from server: {}'.format(server.name))


bot.run(config.token)
