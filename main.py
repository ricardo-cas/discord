import discord
import os
import requests
import json
import random

client = discord.Client()
token = os.environ.get('DISCORD_MOTIVACIONAL_BOT')

lista_triste = ['triste','tristeza','desgosto','abatimento','melancolia','desânimo','mágoa','tédio','aborrecimento','depressão','depressivo','depre','deprê','tedio']

def gera_frase():
  response = requests.get('https://zenquotes.io/api/random')
  dados_json = json.loads(response.text)
  quote = dados_json[0]['q'] + " - " + dados_json[0]['a']
  return(quote)

@client.event
async def on_ready():
    print ('Você está logado como {0.user}. Bot Rodando....'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('/oi'):
        await message.channel.send('Olá, eu sou o Motivacional Bot! =)')
    
    if msg.startswith('/frase'):
        frase = gera_frase()
        await message.channel.send(frase)

    if msg.startswith('/motiva'):
      motiva = ler_json()
      motiva_frase = random.choice(dados)
      frase_final = motiva_frase['frase']+ " - " + motiva_frase['autor']

      await message.channel.send(frase_final)
    
    if any(palavra in msg for palavra in lista_triste):
      motiva = ler_json()
      motiva_frase = random.choice(dados)
      frase_final = motiva_frase['frase']+ " - " + motiva_frase['autor']

      await message.channel.send(frase_final)
 
def ler_json():
    with open('./frases.json', 'r', encoding='UTF-8') as arquivo:
        return json.load(arquivo)

dados = ler_json()

client.run(os.environ.get('DISCORD_MOTIVACIONAL_BOT'))