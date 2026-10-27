import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def stock_dashboard():
    print("=" * 45)
    print("       STOCK MARKET DASHBOARD")
    print("=" * 45)

    symbol = input(
        "Enter stock symbol (e.g., AAPL, MSFT, RELIANCE.NS): "
    ).strip().upper()

    period = input(
        "Enter period (1mo, 3mo, 6mo, 1y): "
    ).strip().lower()

    if period not in ["1mo", "3mo", "6mo", "1y"]:
        period = "1mo"

    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period=period)

        if data.empty:
            print("No stock data found. Check the symbol.")
            return

        latest = data.iloc[-1]
        previous = data.iloc[-2] if len(data) > 1 else latest

        change = latest["Close"] - previous["Close"]
        percent = (
            (change / previous["Close"]) * 100
            if previous["Close"] != 0 else 0
        )

        print("\n" + "=" * 45)
        print("           STOCK INFORMATION")
        print("=" * 45)
        print(f"Stock Symbol : {symbol}")
        print(f"Date         : {data.index[-1].date()}")
        print(f"Open Price   : {latest['Open']:.2f}")
        print(f"High Price   : {latest['High']:.2f}")
        print(f"Low Price    : {latest['Low']:.2f}")
        print(f"Close Price  : {latest['Close']:.2f}")
        print(f"Volume       : {int(latest['Volume']):,}")
        print(f"Price Change : {change:+.2f}")
        print(f"Change (%)   : {percent:+.2f}%")
        print("=" * 45)

        # Display historical stock price chart
        plt.figure(figsize=(10, 5))
        plt.plot(
            data.index,
            data["Close"],
            label="Closing Price"
        )
        plt.title(f"Stock Market Dashboard - {symbol}")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Display recent stock records
        print("\nRecent Stock Records:")
        print(data[["Open", "High", "Low", "Close", "Volume"]].tail())

    except Exception as error:
        print("Error fetching stock data:", error)


if __name__ == "__main__":
    stock_dashboard()
