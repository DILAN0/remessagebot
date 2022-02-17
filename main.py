import discord
from discord.ext import commands

from Token import key

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.' , intents = intents)

token = key

@bot.event
async def on_message(message):

    if message.channel.id == "id":
        otvet = message.content
        channel = bot.get_channel("id")
        await channel.send(otvet)
    else:
        pass

bot.run(token)


