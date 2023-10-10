import discord
from discord.ext import commands
from keys import *

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    parts = message.content.split('|')

    if len(parts) == 3:
        TeamName = parts[0]
        TeamTag = parts[1]
        TeamManagerId = parts[2].strip()  

        try:
            server = message.guild

            user = await server.fetch_member(int(TeamManagerId))

            role = discord.utils.get(server.roles, id=cap_role_id)

            if user and role:
                await user.add_roles(role)
                await message.channel.send(f'Роль {role.name} була додана користувачу {user.display_name}')
            else:
                await message.channel.send('Не вдалося знайти користувача або роль')
        except Exception as e:
            await message.channel.send(f'Виникла помилка: {e}')
    else:
        await message.channel.send("Заявка подана не правильно")

bot.run(TOKEN)