from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from carddata import CardData


class BaseCrawler(ABC):
    def __init__(self):
        self._results = []
    def getCardsData(self, cardlist):
        self._loadSite()
        for card_name in cardlist :
            self._searchForCard(card_name)
            self._getCardElements(card_name)
        return self._results
    def ElementExists(self,elem,xpath):
        try:
            elem.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    def _AddDefaultCard(self, card_name, store):
            self._AddCard(card_name, 0, store, False, 0, 'None')

    def _AddCard(self, name, price, store, foil, stock, edition):
        card_data = {}
        card_data[CardData.NAME]    = name
        card_data[CardData.STORE]    = store
        card_data[CardData.STOCK]   = stock
        card_data[CardData.PRICE]   = price
        card_data[CardData.EDITION] = edition
        card_data[CardData.FOIL] = foil
        self._results.append(card_data)

    @abstractmethod
    def _loadSite(self):
        pass 
    @abstractmethod
    def _searchForCard(self, card_name):
        pass
    @abstractmethod
    def _getCardElements(self, card_name):
        pass

        
