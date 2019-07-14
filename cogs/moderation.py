import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True, administrator=True)
    @commands.bot_has_permissions(kick_members=True, administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick Members from the Server"""
        await ctx.guild.kick(member, reason=reason)
        print('Kicked {0} from {1}'.format(member.name, ctx.guild.name))

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify a member to kick!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('Unable to find member')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You need the Kick Members permission!')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I need the Kick Members permission!')

        print(error)

def setup(bot):
    bot.add_cog(Moderation(bot))
