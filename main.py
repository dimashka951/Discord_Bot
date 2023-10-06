import discord
from discord.ext import commands
from keys import *

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    x
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    parts = message.content.split('|')

    if len(parts) == 3:
        TeamName = parts[0]
        TeamTag = parts[1]
        TeamManagerId = parts[2].strip()  # Очищуємо вхідний рядок від зайвих пробілів

        try:
        # Отримуємо сервер, на якому було відправлено повідомлення
            server = message.guild

        # Отримуємо об'єкт користувача за його ідентифікатором
            user = await server.fetch_member(int(TeamManagerId))

        # Знаходимо роль, яку потрібно додати за ідентифікатором
            role = discord.utils.get(server.roles, id=cap_role_id)  # Перед цим потрібно мати змінну TeamManagerRoleId

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