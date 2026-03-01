# using yfinance Library to Extract stock data
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt



# Using the Ticker module we can create an object that will allow us to access functions
#  to extract data. To do this we need to provide the ticker symbol for the stock, 
# here the company is Apple and the ticker symbol is AAPL.




# Create ticker object
apple = yf.Ticker("AAPL")

# Get company information
apple_info = apple.info

# Access country
print(apple_info['country'])

# Get Historical Share Price Data
apple_share_price_data = apple.history(period="max")


# Preview Data
apple_share_price_data.head()

# Reset Index
apple_share_price_data.reset_index(inplace=True)


# Plot Open Price vs Date
apple_share_price_data.plot(x="Date", y="Open", title="Apple Stock Open Price")

# Show plot
plt.show()