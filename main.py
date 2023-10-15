# main.py
import asyncio
import discord
from discord.ext import commands
from keys import *
import os

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

async def load_extensions():
    for filename in os.listdir("./modules"):
        if filename.endswith(".py"):
            await client.load_extension(f"modules.{filename[:-3]}")

async def setup():
    await load_extensions()
    await client.start(TOKEN)

loop = asyncio.get_event_loop()
loop.run_until_complete(setup())