import crawlers.webcrawler as Base
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Create a webcrawler that navigates over dracoti's site and 
# checks for the given list of cards
# returns a dictionary with the price and stock information avalable with the card name as the key
class Dracoti(Base.BaseCrawler):
    def __init__(self,driver):
        self.__url = "https://shop.dracoti.co.za"
        self.__driver = driver
        self.__sb_name = "rs"

    def getCardsData(self, cardlist):
        self.__loadSite()
        for card in cardlist :
            self.__searchForCard(card)
            self.__getCardElements()
            
            
    def __loadSite(self):
        self.__driver.get(self.__url)

    def __searchForCard(self, card):
        search_elem = self.__driver.find_element_by_name(self.__sb_name)
        search_elem.clear()
        search_elem.send_keys(card)
        search_elem.send_keys(Keys.RETURN)

    def __getCardElements(self):
        if self.__NoStock():
            return
        
        cards_found = self.__driver.find_elements_by_xpath("//div[@class = 'rs_content']")
        for card in cards_found:
            stock  = self.__getStockValue(card)


    def __NoStock(self):
        try:
            self.__driver.find_element_by_xpath("//p[@class = 'rs_result_heading']")
        except NoSuchElementException:
            return False
        return True

    def __getStockValue(self, card):
        stock = card.find_element_by_xpath("//span[@class = 'stock in-stock']")
        stock_value = int(stock.text.replace( " in stock", ""))
        return stock_value

        
        