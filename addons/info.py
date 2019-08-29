import discord
from discord.ext import commands
from sys import argv

class Information:
    """
        Shows information about the clan
    """
    def __init__(self, bot):
        self.bot = bot
        print('Addon "{}" loaded'.format(self.__class__.__name__))

    @commands.command(pass_context=True)
    async def site(self, ctx):
        """Display Site URL."""
        await self.bot.say("https://legacy-rs.org")

    @commands.command(pass_context=True)
    async def ts(self, ctx):
        """Display TS Address."""
        await self.bot.say("ts.legacy-rs.org")

    @commands.command(pass_context=True)
    async def apply(self, ctx):
        """Display Application Form."""
        await self.bot.say("https://legacy-rs.org/forum/5-member-applications-open/?do=add")

# Load the extension
def setup(bot):
    bot.add_cog(Information(bot))

