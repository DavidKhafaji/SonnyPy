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
        await self.bot.say("https://unt.edu/")

    @commands.command(pass_context=True)
    async def ts(self, ctx):
        """Display Canvas Address."""
        await self.bot.say("https://unt.instructure.com/")

    @commands.command(pass_context=True)
    async def apply(self, ctx):
        """Display Admissions."""
        await self.bot.say("https://admissions.unt.edu/")

# Load the extension
def setup(bot):
    bot.add_cog(Information(bot))

