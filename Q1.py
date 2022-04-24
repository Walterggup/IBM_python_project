# Question 1 Reset the index, save, and display the first five rows of the tesla_data dataframe 
# using the head function. Upload a screenshot of the results and code from the beginning of 
# Question 1 to the results below.
import yfinance as yf

Tesla = yf.Ticker("TSLA")
tesla_data = Tesla.history(period="max")
tesla_data.reset_index(inplace =True)
tesla_data.head()
print (tesla_data)