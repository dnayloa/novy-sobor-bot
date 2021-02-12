import discord
import os
from osrs_api import GrandExchange
from osrs_api import Item
from osrsquery import OSRSQuery

client = discord.Client()
osrs_query = OSRSQuery()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/ge_price'):
        await message.channel.send(osrs_query.grand_enchange_price(message.content))

    if message.content.startswith('/ge_trend'):
        await message.channel.send(osrs_query.grand_enchange_price(message.content))

client.run(os.getenv('TOKEN'))


