import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-------------------")

client.run(TOKEN)