from selenium import webdriver
from crawlers.dracoti import Dracoti


cardlist = ["wall of roots"]
driver = webdriver.Chrome()
dracoti = Dracoti(driver)
dracoti.getCardsData(cardlist)
driver.close()