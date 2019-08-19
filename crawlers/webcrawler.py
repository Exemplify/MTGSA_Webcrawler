from abc import ABC, abstractmethod

class BaseCrawler(ABC):
    def getSiteData(self, driver):
        pass
