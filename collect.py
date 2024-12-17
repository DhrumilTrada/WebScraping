from bs4 import BeautifulSoup
import os
import pandas as pd


d = {'Title':[],'Price':[],'MRP':[],'Discount':[],'Reviews':[]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.find("h2").get_text()
        price = float("".join((soup.find("span", attrs={"class" : 'a-price-whole'}).get_text()).split(",")))
        reviews = (soup.find("span", attrs={"class": "a-icon-alt"}).get_text())[0:3]
        mrp = float("".join(((soup.findAll("span", attrs={"class": "a-offscreen"})[1].get_text())[3:]).split(",")))
        discount = float((mrp - price)/mrp) * 100
        d["Discount"].append(discount)
        d["MRP"].append(mrp)
        d["Title"].append(title)
        d["Price"].append(price)
        d["Reviews"].append(reviews)
    except Exception as e:
        print("", end="")
     

df = pd.DataFrame(data = d)
print(df)
df.to_csv("data.csv")
