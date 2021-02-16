from osrsbox import items_api
from GrandExchange import GrandExchange
import pprint as pp
import discord
import requests


class OSRSQuery:

    def __init__ (self):
        self.all_db_items = items_api.load()
        self.exchange = GrandExchange.Exchange()

    def item_value(self, name):
        try:
            item = self.all_db_items.lookup_by_item_name(name)
            
            embed = discord.Embed(title = item.name, url = item.wiki_url, color = discord.Color.blue())
            embed.add_field(name = "Sell Average: ", value = "{:,} gp".format(self.exchange.get_item(item.name).overall_average, inline=False))
            embed.add_field(name = "Buy Average: ", value = "{:,} gp".format(self.exchange.get_item(item.name).buy_average), inline=False)
            embed.add_field(name = "High Alc: ", value = "{:,}".format(item.highalch), inline=False)
            embed.add_field(name = "Low Alc: ", value = "{:,}".format(item.lowalch), inline=False)
        except(ValueError):
            embed = discord.Embed(title = "Error !", color = discord.Color.red(), description = "Cannot find the provided item name...)")
        return embed

osrsquery = OSRSQuery()

