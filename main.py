import discord
import os
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
async def _ge(ctx, arg):
    await ctx.send(embed=osrs.item_value(arg))

    # if message.content.startswith('/ge_trend'):
    #     await message.channel.send(osrs_query.grand_enchange_price(message.content))

bot.run(config('TOKEN'))


