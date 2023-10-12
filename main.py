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

    
    if message.author == client.user:
        return

    if message.channel.id == regChat:
        checkMessage = message.content.split('|')

        try:

            tname = checkMessage[0]
            ttag = checkMessage[1]
            tmanager = checkMessage[2][3:-1].strip()

            guild = message.guild
            role = discord.utils.get(guild.roles, id=cap_role_id)
            member = guild.get_member(int(tmanager))

            await member.add_roles(role)
        except:
            await message.add_reaction(em_not_correct)
        else:
            if len(Team.teamlist) <=16:
                await message.add_reaction(em_correct)
                
                teamToTeamList = Team(tname, ttag, tmanager)
                Team.teamlist.append([teamToTeamList.name, teamToTeamList.tag, teamToTeamList.meneger])
            else:
                await message.add_reaction(em_not_correct)

    if len(Team.teamlist) == 16:  
        await message.channel.send("Teamlist full")
        print(Team.teamlist)
        



client.run(TOKEN)
