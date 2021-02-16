import discord
import os
import requests
import json
from discord.ext import commands

from osrsquery import OSRSQuery
from decouple import config

bot = commands.Bot(command_prefix="!")
# bot = discord.Client()

osrs = OSRSQuery() 


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def on_message(message):
    if message.author == bot.user:
        return


@bot.command(name='ge')
async def _ge(ctx, *args):
    item = " ".join(list(args))                         #convert list of args into searchable item name
    await ctx.send(embed = osrs.item_value(item))

@bot.command(name='qod')
async def _qod(ctx, arg = ""):
    msg = ""
    try:
        qod = requests.get('https://quotes.rest/qod?language=en').text
        msg = str(qod.contents.quotes)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        msg = str(e)

    await ctx.send(msg)

bot.run(config('TOKEN'))


