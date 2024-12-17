import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import os
import pandas as pd


data = {'Title':[],'Price':[],'MRP':[],'Discount':[],'Reviews':[]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.find("h2").get_text()
        price = float("".join((soup.find("span", attrs={"class" : 'a-price-whole'}).get_text()).split(",")))
        reviews = float((soup.find("span", attrs={"class": "a-icon-alt"}).get_text())[0:3])
        mrp = float("".join(((soup.findAll("span", attrs={"class": "a-offscreen"})[1].get_text())[3:]).split(",")))
        discount = float((mrp - price)/mrp) * 100
        data["Discount"].append(discount)
        data["MRP"].append(mrp)
        data["Title"].append(title)
        data["Price"].append(price)
        data["Reviews"].append(reviews)
    except Exception as e:
        print("", end="")
     

df = pd.DataFrame(data = data)
print(df)
df.to_csv("data.csv")

# Set Seaborn Style
sns.set_theme(style="whitegrid")

# 1. Price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Price'], kde=True, color='blue')
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()

# 2. Discount Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Discount'], kde=True, color='red')
plt.title("Discount Distribution")
plt.xlabel("Discount")
plt.ylabel("Count")
plt.show()

# 3. Reviews Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Reviews'], bins=8, kde=True, color='green')
plt.title("Reviews Distribution")
plt.xlabel("Reviews")
plt.ylabel("Count")
plt.show()

# 4. Top 5 Products by Price
top_price = df.nlargest(5, 'Price')
plt.figure(figsize=(12, 6))
sns.barplot(data=top_price, x='Price', y='Title', palette='viridis')
plt.title("Top 5 Products by Price")
plt.xlabel("Price")
plt.ylabel("Title")
plt.show()

# 5. Bottom 5 Products by Reviews
bottom_reviews = df.nsmallest(5, 'Reviews')
plt.figure(figsize=(12, 6))
sns.barplot(data=bottom_reviews, x='Reviews', y='Title', palette='magma')
plt.title("Bottom 5 Products by Reviews")
plt.xlabel("Reviews")
plt.ylabel("Title")
plt.show()

# 6. Price vs MRP with Discounts (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Price', y='MRP', size='Discount', hue='Reviews', palette='coolwarm', sizes=(50, 300))
plt.title("Price vs MRP with Discount Sizes and Review Colors")
plt.xlabel("Price")
plt.ylabel("MRP")
plt.legend(title="Reviews")
plt.show()
