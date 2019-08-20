import crawlers.webcrawler as Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from carddata import CardData

# Create a webcrawler that navigates over Topdeck's site and 
# checks for the given list of cards
# returns a dictionary with the price and stock information avalable with the card name as the key
class Topdeck(Base.BaseCrawler):
    def __init__(self,driver):
        super().__init__()
        self.__url = "https://store.topdecksa.co.za"
        self.__driver = driver
        self.__store_name = "Topdeck"     
            
    def _loadSite(self):
        self.__driver.get(self.__url)

    def _searchForCard(self, card_name):
        search_elem = self.__driver.find_element_by_xpath("//input[@id = 'search-input']")
        search_elem.clear()
        search_elem.send_keys(card_name)
        search_elem.send_keys(Keys.RETURN)

    def _getCardElements(self, card_name):

        if not self.__InStock():
            self._AddDefaultCard(card_name, self.__store_name)
            return

        wait = WebDriverWait(self.__driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class = 'grid-image']/a[@class = 'grid-image--centered']/img")))
        cards_found = self.__driver.find_elements_by_xpath("//div[@class = 'product-item fluid-grid-item text-center']")
        for card in cards_found:
            card_descrip = card.find_element_by_xpath("./p[@class = 'product-item__name']").text.split('\n')
            if(card_name not in card_descrip[0]):
                continue
            self._AddCard( card_name,self.__getPriceValue(card),self.__store_name, \
                           self.__getFoilValue(card_descrip), self.__getStockValue(card_descrip),  \
                           self.__getEditionValue(card_descrip))
            
    def __InStock(self):
       return self.ElementExists(self.__driver, "//div[@class = 'product-item fluid-grid-item text-center']")

    def __getStockValue(self, card_descrip):
        stock_value = int(card_descrip[2].replace( " in stock", ""))
        return stock_value

    def __getPriceValue(self, card):
        price = card.find_element_by_xpath("./p[@class= 'product-item__price']").text
        price_value = float(price.replace('R ', ''))
        return price_value

    def __getEditionValue(self,card_descrip):
        return card_descrip[1].replace('(Foil)', '')
        
    def __getFoilValue(self,card_descrip):
        edition_lower = card_descrip[1].lower()
        return 'foil' in edition_lower

            
