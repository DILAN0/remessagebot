import discord
from discord.ext import commands

from Token import key

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.' , intents = intents)

token = key

@bot.event
async def on_message(message):

    if message.channel.id == 792491223495606352:
        otvet = message.content
        channel = bot.get_channel(712296555985764435)
        await channel.send(otvet)
    else:
        pass

bot.run(token)


