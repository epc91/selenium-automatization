from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path='/home/epc91/mozilla-webdriver/geckodriver')

with open("data.json") as json_file:
    data = json.load(json_file)

    for p in data["employees"]:
        print(p["name"] + " is loading!")
        driver.get("https://www.google.com/?hl=es")
        time.sleep(2)

driver.close()