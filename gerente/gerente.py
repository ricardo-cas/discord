import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import requests
import json
import random
from keep_alive import keep_alive
import asyncio
import datetime as DT       # Imports datetime as DT so instead of typing 'datetime.datetime.now()' you type 'DT.datetime.now()' it saves time and looks less dumb than 'datetime.datetime.now()'
from time import sleep      # Imports sleep because time.sleep() doesn't work
# import sLOUT as lout


client = commands.Bot(command_prefix = '.')
token = os.environ.get('DISCORD_MANAGER_BOT')

# Checks time that bot was started
botStartTime = DT.datetime.now()

# Store the bot version and release date
ver = ['v1.0.0', '2021-01-03']

# Define a config file for use in the log commands. 
config = 'config.yml'

@client.event
async def on_ready():
  # frase no console para verificar se o bot está on-line
    print ('Você está logado como {0.user}. Bot Manager Rodando... ²º²¹'.format(client))
    # definindo a frase do jogo que o bot estará "jogando"
    game = discord.Game("De olho em você ...")
    # definindo o status do bot para "não pertube" e o jogo que ele está jogando
    await client.change_presence(status=discord.Status.dnd, activity=game)

@client.command()
async def ping(ctx):
  embed = discord.Embed(
        color = discord.Color.red()
    )
  # await ctx.send(embed=embed)
  await ctx.send(f'Pong! \nSeu ping é {round(client.latency * 1000)} ms')
  return 

@client.command()
async def limpar(ctx, minimo=5):
  await ctx.channel.purge(limit=minimo)
  channel = client.get_channel(795392412960555029)
  await channel.send(f'{minimo} mensagens deletadas no canal')
  print(f"Usuário {discord.abc.User.mention} apagou {minimo} Mensagens deletadas")

@client.command()
async def ola(ctx):
  await ctx.send('Oi! Tudo bem?')

@client.command()
async def oi(ctx):
  await ctx.send('Oi! Tudo bem?')


# Info Command
@client.command(pass_context=True)
async def info(ctx):
    startTime = DT.datetime.now()       # Get the time the command was initiated at
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name='Need Help?', value='You can get help by creating an issue on our [GitHub](https://github.com/Sidpatchy/RomeBot/issues) or by joining our [support server](https://discord.gg/NwQUkZQ)')
    embed.add_field(name='Add Me to a Server', value='Adding me to a server is simple, all you have to do is click [here](https://discord.bots.gg/bots/511050489928876052)')
    embed.add_field(name='GitHub', value='RomeBot is open source, that means you can view all of its code! Check out its [GitHub!](https://github.com/Sidpatchy/RomeBot)')
    await ctx.send(embed=embed)             # Send the embed created above in the channel the command was run in.
    # lout.log(config, startTime, 'info')     # Write to log

# !time, states the server time
@client.command(pass_context=True)
async def time(ctx):
    startTime = DT.datetime.now()
    await ctx.send('Server time is: {}'.format(DT.datetime.now()))
    # lout.log(config, startTime, 'time')


# keep_alive()
client.run(os.environ.get('DISCORD_MANAGER_BOT'))