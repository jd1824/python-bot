import requests
import json
import discord
from discord.ext import commands

url = "https://pokeapi.co/api/v2/pokemon/"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
intents.message_content = True

bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def poke(ctx, num: int):
    url2 = url + str(num)
    poke = requests.get(url2)
    poke_s = poke.text
    poke_r = json.loads(poke_s)
   # print(poke_r["name"])
  
    await ctx.send(poke_r["name"])

@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)

@bot.command(name="info")
async def info(ctx):
    embed = discord.Embed(title="informacion", description="este es un pequeño bot de prueba en python", color=discord.Color.blue())
    embed.add_field(name='campo1', value='pruebs', inline=False)
    #embed.add_field(name='Campo 2', value='Valor 2', inline=False)
    embed.set_footer(text='ejemplo')

    await ctx.send(embed=embed)




bot.run("token")
