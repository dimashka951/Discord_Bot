import discord
from discord.ext import commands
from keys import *
client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-------------------")


    
print("hello")
client.run(TOKEN)