import pandas as pd
import matplotlib.pyplot as plt

# Ensure Date columns are datetime
gme_data["Date"] = pd.to_datetime(gme_data["Date"])
gme_revenue["Date"] = pd.to_datetime(gme_revenue["Date"])

# Function to create the graph
def make_graph(stock_data, revenue_data, stock):
    
    stock_data_specific = stock_data[stock_data["Date"] <= "2021-06-14"]
    revenue_data_specific = revenue_data[revenue_data["Date"] <= "2021-04-30"]

    fig, axes = plt.subplots(2, 1, figsize=(12,8), sharex=True)

    # Stock price graph
    axes[0].plot(stock_data_specific["Date"],
                 stock_data_specific["Close"].astype(float))
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue graph
    axes[1].plot(revenue_data_specific["Date"],
                 revenue_data_specific["Revenue"].astype(float))
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

# Call the function
make_graph(gme_data, gme_revenue, "GameStop")