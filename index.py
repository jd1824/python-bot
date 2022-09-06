import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)

bot.run("MTAxNjUxMDgxMTEwMDk1NDY1NQ.GwTjOO.Qx-d7xxyOC_rYhkPvMxoB3mFsQgi05vqiZBZU4")