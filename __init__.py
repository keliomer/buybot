import requests
from bs4 import BeautifulSoup


class SupremeBot(object):

    def __init__(self):
        """Set up attributes for the bot"""
        # self.billing_address = bill
        # self.shipping_address = ship
        self.url = "https://supremenewyork.com"
        self.main_page = self.parse_webpage(self.url + "/shop" )
        self.item_urls = self.get_item_urls()



    def parse_webpage(self, url):
        """Go to url and get HTML from page"""
        r = requests.get(url)
        page = r.text
        info = BeautifulSoup(page, 'html.parser')
        return info

    def get_item_urls(self):
        """Gets list of items in store"""
        # We know the shop is in one of the uls from the source code but
        # the order may change
        # New items are released every week and the other uls don't use
        # new to describe anything on the page
        # That means we can use new as a search key for finding the shop
        # The we find all the li in the shop as they contain items (urls and images)
        # then we return a list of item urls


        # Look at get_item_prices and use the find method properly to locate the store
        ul_list = self.main_page.find_all('ul')
        for ul in ul_list:
            if 'new' in ul.text:
                items = ul.find_all('li')


        return [self.url + item.a['href'] for item in items]

    def get_item_prices(self):
        """Get Item Prices"""
        # empty list to put prices in
        prices = []
        # Go through each item url and get necessary info
        for url in self.item_urls:
            info = self.parse_webpage(url)
            # THIS IS HOW YOU PROPERLY USE BS4.Find
            name = info.find('h1', {'itemprop': 'name'})
            price = info.find('span', {'itemprop': 'price'})
            # add price of current item to prices
            prices.append((name.text, price.text))
        return prices