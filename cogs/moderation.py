import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Ban', pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban Members from the Server"""
        await ctx.guild.ban(member, reason=reason)
        name = member.name + '#' + member.discriminator
        await ctx.send('{0} has been banned'.format(name))
        print('Banned {0} from {1}'.format(name, ctx.guild.name))

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the Ban Members permission!')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I do not have the Ban Members permission!')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify a member to ban!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('Unable to find member')

    @commands.command(name='Kick', pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick Members from the Server"""
        await ctx.guild.kick(member, reason=reason)
        name = member.name + '#' + member.discriminator
        await ctx.send('{0} has been kicked'.format(name))
        print('Kicked {0} from {1}'.format(name, ctx.guild.name))

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the Kick Members permission!')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('I do not have the Kick Members permission!')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify a member to kick!')
        elif isinstance(error, commands.BadArgument):
            await ctx.send('Unable to find member')


def setup(bot):
    bot.add_cog(Moderation(bot))
