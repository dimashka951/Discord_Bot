# teamlistcog.py

import discord
from discord.ext import commands
from keys import *

class TeamlistCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def show_teamlist(self, ctx):
        if teamlist:
            slot = 3
            for team in teamlist:
                await ctx.send(slot + " | " + team[0] + " || " + team[2])
                slot+=1
        else:
            await ctx.send("Teamlist is empty")

    @commands.command()
    async def clear_teamlist(self, ctx):
        teamlist.clear()
        await ctx.send("Team List has been cleared.")

async def setup(client):
    await client.add_cog(TeamlistCog(client))