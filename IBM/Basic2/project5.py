# Install yfinance if needed
# !pip install yfinance

import yfinance as yf
import pandas as pd

# Create ticker object for GameStop
gme = yf.Ticker("GME")

# Extract stock data for the maximum available period
gme_data = gme.history(period="max")

# Reset the index
gme_data.reset_index(inplace=True)

# Display first 5 rows
gme_data.head()