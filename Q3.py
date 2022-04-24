# Question 3: Use yfinance to Extract Stock Data
#Reset the index, save, and display the first five rows of the gme_data dataframe
#  using the head function. Upload a screenshot of the results and 
# code from the beginning of Question 1 to the results below.

import yfinance as yf 

GME = yf.Ticker("GME")
gme_data = GME.history(period = 'max')
gme_data.reset_index(inplace = True)
print(gme_data.head())