import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready and on-line')


client.run('NzkyNDA5MTg1NTI5NjI2NjQ1.X-dSkA.b1OeKQwj_Wdf4O27h_04EeSFgvc')