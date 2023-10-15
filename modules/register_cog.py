
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
            check_message = message.content.split('|')
            guild = message.guild
            role = discord.utils.get(guild.roles, id=cap_role_id)

            try:
                team_manager = check_message[2][3:-1].strip()
                member = guild.get_member(int(team_manager))

                await member.add_roles(role)
            except:
                await message.add_reaction(em_not_correct)
            else:
                if len(teamlist) <= 16 and len(check_message) == 3:
                    await message.add_reaction(em_correct)

                    teamlist.append(check_message)
                else:
                    await message.add_reaction(em_not_correct)

        if len(teamlist) == 16:
            await message.channel.send("Teamlist full")
            print("length: " + str(len(teamlist)))
            slot = 3
            for team in teamlist:
                print(str(slot) + " | " + team[0] + " / " + team[1] + " // " + team[2])
                print('----------------------------------------------')
                slot += 1

async def setup(client):
    await client.add_cog(RegisterCog(client))
