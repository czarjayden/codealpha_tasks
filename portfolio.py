import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker}.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if self.portfolio[ticker] > shares:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker}.")
            elif self.portfolio[ticker] == shares:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker}.")
            else:
                print(f"Not enough shares to remove. You only have {self.portfolio[ticker]} shares.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def fetch_stock_price(self, ticker):
        api_key = "REST API"
        url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['price']
            else:
                print(f"No data found for {ticker}.")
        else:
            print(f"Failed to fetch data for {ticker}. Status code: {response.status_code}")
        return None

    def track_performance(self):
        print("\nPortfolio Performance:")
        for ticker, shares in self.portfolio.items():
            price = self.fetch_stock_price(ticker)
            if price:
                print(f"{ticker}: {shares} shares @ ${price:.2f} each (${shares * price:.2f} total)")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    portfolio.add_stock("AAPL", 10)
    portfolio.add_stock("GOOGL", 5)
    portfolio.track_performance()
    portfolio.remove_stock("AAPL", 5)
    portfolio.track_performance()