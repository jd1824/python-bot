import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='>', intents=discord.Intents.default())

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)


bot.run(token)
