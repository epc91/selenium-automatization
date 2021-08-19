from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path='/home/epc91/mozilla-webdriver/geckodriver')

with open("data.json") as json_file:
    data = json.load(json_file)

    for p in data["searches"]:
        print("Searching" + p["text"] + "!")
        driver.get("https://www.google.com/?hl=es")
        time.sleep(3)

        # Search
        searchGoogleField = driver.find_element_by_class_name("gLFyf.gsfi")
        searchGoogleField.send_keys(p["text"])
        searchGoogleField.send_keys(Keys.ENTER)
        time.sleep(3)

driver.close()
print("Exit!")