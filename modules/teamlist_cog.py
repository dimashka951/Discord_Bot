import discord
from discord.ext import commands
from keys import *

class TeamlistCog(commands.Cog):
    def __init__(self, client):
        self.client = client


async def setup(client):
    await client.add_cog(TeamlistCog(client))