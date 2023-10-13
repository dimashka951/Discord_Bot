# main.py
import discord
from discord.ext import commands
from keys import *
import os

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    await client.process_commands(message)

for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
