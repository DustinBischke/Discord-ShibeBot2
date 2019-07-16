import discord
import os
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Reload', pass_context=True)
    @commands.is_owner()
    async def reload(self, ctx):
        """Reloads all Modules"""
        cogs = os.listdir('cogs')

        if '__pycache__' in cogs:
            cogs.remove('__pycache__')

        for cog in cogs:
            cog = cog.replace('.py', '')
            self.bot.unload_extension('cogs.{}'.format(cog))
            self.bot.load_extension('cogs.{}'.format(cog))

        await ctx.send('Reloaded modules')
        print('Reloaded modules')

def setup(bot):
    bot.add_cog(Admin(bot))
