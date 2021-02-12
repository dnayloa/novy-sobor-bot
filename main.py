import discord
import os

from osrsquery import OSRSQuery
from decouple import config

client = discord.Client()
osrs_query = OSRSQuery()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('/ge'):
        item_name = message.content[4:]
        await message.channel.send(embed=osrs_query.item_value(item_name))

    # if message.content.startswith('/ge_trend'):
    #     await message.channel.send(osrs_query.grand_enchange_price(message.content))

client.run(config('TOKEN'))


