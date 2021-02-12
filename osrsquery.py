from osrs_api import GrandExchange
from osrs_api import Item

class OSRSQuery:

    def grand_enchange_price(self, msg):
        item_name = msg[10:]
        item_id = Item.get_ids(item_name)
        item = GrandExchange.item(item_id)
        return "Item: "+ item_name + " is " + str("{:,.2f}".format(item.price())) + " gp"

    def grand_enchange_trend(self, msg):
        query = msg[10:]
        time = query.split()[0]
        item_name = ""
        item_id = Item.get_ids(item_name)
        item = GrandExchange.item(item_id)
        return "Item: "+ item_name + " is " + str("{:,.2f}".format(item.price())) + " gp"
