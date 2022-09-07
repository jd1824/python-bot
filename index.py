import discord
from discord.ext import commands

Intents = discord.Intents.default()
Intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=Intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)


bot.run("token")
