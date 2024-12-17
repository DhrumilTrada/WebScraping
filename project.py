from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = input("Enter the product to search: ")
file = 0
for i in range(1, 20):
    driver.get(f"http://www.amazon.in/s?k={query}&page={i}&crid=234WC15ZUST3N&sprefix=lap%2Caps%2C432&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w",encoding = "utf-8") as f:
            if d is not None:
                f.write(d)

            file +=1


    time.sleep(2)
driver.close()
