from crawlers.webcrawler import BaseCrawler

# Create a webcrawler that navigates over dracoti's site and 
# checks for the given list of cards
# returns a dictionary with the price and stock information avalable with the card name as the key
class Dracoti(BaseCrawler):
    def __init__(self):
        self.__url = "https://shop.dracoti.co.za"
        pass
    def getCardsData(self, driver, cardlist):
        pass
    def __loadSite(self):
        pass 
    def __searchForCards(self, list):
        pass
    def __getStockCount(self):
        pass
    def __getPrice(self):
        pass
        
