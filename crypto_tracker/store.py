import pandas as pd
from collections import deque

class PriceStore:
    def __init__(self, max_length=300):
        self.prices = deque(maxlen=max_length)

    def add_price(self, price):
        self.prices.append(price)

    def get_dataframe(self):
        return pd.DataFrame({"price": list(self.prices)})

    def moving_average(self, window=20):
        df = self.get_dataframe()
        if len(df) >= window:
            return df["price"].rolling(window).mean().iloc[-1]
        return None
