import discord
from discord.ext import commands
from keys import *

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    await client.process_commands(message)

    while len(TeamList) <= 16: 
        if message.author == client.user:
            return

        if message.channel.id == regChat:
            teamToTeamList = message.content.split('|')

            try:
                tname = teamToTeamList[0]
                ttag = teamToTeamList[1]
                tmanager = teamToTeamList[2][3:-1].strip()

                guild = message.guild
                role = discord.utils.get(guild.roles, id=cap_role_id)
                member = guild.get_member(int(tmanager))

                await member.add_roles(role)
            except:
                await message.add_reaction(em_not_correct)
            else:
                await message.add_reaction(em_correct)
                TeamList.append([tname, ttag, tmanager])

    if len(TeamList) == 16:  
        await message.channel.send("Teamlist full")
        



client.run(TOKEN)
