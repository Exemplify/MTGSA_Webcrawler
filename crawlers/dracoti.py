import crawlers.webcrawler as Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from carddata import CardData

# Create a webcrawler that navigates over dracoti's site and 
# checks for the given list of cards
# returns a dictionary with the price and stock information avalable with the card name as the key
class Dracoti(Base.BaseCrawler):
    def __init__(self,driver):
        super().__init__()
        self.__url = "https://shop.dracoti.co.za"
        self.__driver = driver
        self.__sb_name = "rs"
        self.__store_name = "Dracoti"     
            
    def _loadSite(self):
        self.__driver.get(self.__url)

    def _searchForCard(self, card_name):
        search_elem = self.__driver.find_element_by_name(self.__sb_name)
        search_elem.clear()
        search_elem.send_keys(card_name)
        search_elem.send_keys(Keys.RETURN)

    def _getCardElements(self, card_name):
        if not self.__InStock():
            self._AddDefaultCard(card_name, self.__store_name)
            return

        wait = WebDriverWait(self.__driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'rs_rs_avatar']/a/img")))
        cards_found = self.__driver.find_elements_by_xpath("//div[@class = 'rs_content']")
        for card in cards_found:
            self._AddCard( card_name,self.__getPriceValue(card),self.__store_name, \
                           self.__getFoilValue(card), self.__getStockValue(card),  \
                           self.__getEditionValue(card))
            

    def __InStock(self):
       return self.ElementExists(self.__driver, "//p[@class = 'rs_result_heading']")

    def __getStockValue(self, card):
        stock = card.find_element_by_xpath("./span[@class = 'rs_rs_stock']//span")
        stock_value = int(stock.text.replace( " in stock", ""))
        return stock_value

    def __getPriceValue(self, card):
        price = card.find_element_by_xpath("./div[@class = 'rs_rs_price']//span[@class = 'woocommerce-Price-amount amount']")
        price_value = float(price.text.replace('R', ''))
        return price_value

    def __getEditionValue(self,card):
        edition = card.find_element_by_xpath("./div[@class = 'rs_rs_cat posted_in']//a[1]")
        return edition.text

    def __getFoilValue(self,card):
        xpath = "./a/span[@class = 'rs_rs_name']"
        name = card.find_element_by_xpath(xpath).text.lower()
        return 'foil' in name

            

        
        