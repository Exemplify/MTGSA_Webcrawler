from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaseCrawler(ABC):
    def getCardsData(self, driver):
        pass
