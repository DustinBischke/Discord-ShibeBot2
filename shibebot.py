import asyncio
import discord
from discord.ext import commands
from utils import config

bot = commands.Bot(command_prefix=config.prefix)

@bot.event
async def on_ready():
    print('Connected as: {}'.format(bot.user.name))
    print('Discord.py Version: {}'.format(discord.__version__))

@bot.event
async def on_server_join(server):
    print('Added to server: {}'.format(server.name))

@bot.event
async def on_server_leave(server):
    print('Removed from server: {}'.format(server.name))

@bot.event
async def on_message(message):
    print('Received message: {}'.format(message.content))
    await bot.process_commands(message)

@bot.command()
async def test():
    await bot.say('Hello world!')

bot.run(config.token)
