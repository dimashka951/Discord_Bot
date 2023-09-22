import discord
from discord.ext import commands
from keys import *
client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-------------------")

@client.event
async def hello(ctx):
    await ctx.send("Hello")
    
client.run(TOKEN)