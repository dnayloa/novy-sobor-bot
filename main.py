import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/ge'):
        await message.channel.send('We cannot search the GE yet, function pending...')

client.run(os.getenv('TOKEN'))

