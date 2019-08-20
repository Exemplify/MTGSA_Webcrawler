from selenium import webdriver
from crawlers.dracoti import Dracoti
from crawlers.topdeck import Topdeck
import csv
from carddata import CardData

cardlist = ["Flickerwisp"]
driver = webdriver.Chrome()
dracoti = Dracoti(driver)
drac_results = dracoti.getCardsData(cardlist)
topdeck = Topdeck(driver)
top_results = topdeck.getCardsData(cardlist)
csv_columns = [CardData.NAME, CardData.STORE, CardData.STOCK, CardData.PRICE, CardData.FOIL, CardData.EDITION]
drac_results.extend(top_results)
dict_data = drac_results
csv_file = "Data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error") 
driver.quit()