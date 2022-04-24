#Question 4: Use Webscraping to Extract GME Revenue Data
#Display the last five rows of the gme_revenue dataframe using the tail function. 
# Upload a screenshot of the results.

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text

soup = BeautifulSoup(html_data, "html.parser")
soup.find_all('title')

GME_revenue = pd.DataFrame(columns = ['Date', 'Revenue'])

for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")
    
    GME_revenue = GME_revenue.append({"Date": date, "Revenue": revenue}, ignore_index = True)

GME_revenue.dropna(inplace=True)
GME_revenue = GME_revenue[GME_revenue['Revenue'] != ""]

print(GME_revenue.tail())