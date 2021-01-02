import discord
import os
import requests
import json
import random
from keep_alive import keep_alive




client = discord.Client()
token = os.environ.get('DISCORD_MANAGER_BOT')

@client.event
async def on_ready():
  # frase no console para verificar se o bot está on-line
    print ('Você está logado como {0.user}. Bot Manager Rodando....123'.format(client))
    # definindo a frase do jogo que o bot estará "jogando"
    game = discord.Game("De olho em você ...")
    # definindo o status do bot para "não pertube" e o jogo que ele está jogando
    await client.change_presence(status=discord.Status.dnd, activity=game)

# keep_alive()
client.run(os.environ.get('DISCORD_MANAGER_BOT'))

