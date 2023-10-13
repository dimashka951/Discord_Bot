import discord
from discord.ext import commands
from keys import *

class RegisterCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
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
                if len(Team.teamlist) <= 16:
                    await message.add_reaction(em_correct)

                    teamToTeamList = Team(tname, ttag, tmanager)
                    Team.teamlist.append([teamToTeamList.name, teamToTeamList.tag, teamToTeamList.meneger])
                else:
                    await message.add_reaction(em_not_correct)

        if len(Team.teamlist) == 16:
            await message.channel.send("Teamlist full")
            print(len(Team.teamlist))

def setup(client):
    client.add_cog(RegisterCog(client))
