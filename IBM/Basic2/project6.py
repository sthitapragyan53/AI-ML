import matplotlib.pyplot as plt
import pandas as pd

# Convert dates first
tesla_data["Date"] = pd.to_datetime(tesla_data["Date"])
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])

def make_graph(stock_data, revenue_data, stock):

    stock_data_specific = stock_data[stock_data["Date"] <= "2021-06-14"]
    revenue_data_specific = revenue_data[revenue_data["Date"] <= "2021-04-30"]

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    axes[0].plot(stock_data_specific["Date"],
                 stock_data_specific["Close"].astype(float))
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    axes[1].plot(revenue_data_specific["Date"],
                 revenue_data_specific["Revenue"].astype(float))
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

# CALL THE FUNCTION
make_graph(tesla_data, tesla_revenue, "Tesla")