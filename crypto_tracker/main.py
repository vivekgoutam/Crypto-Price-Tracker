import asyncio
from tracker import track_price
from store import PriceStore
from plotting import PricePlotter
from alerts import AlertManager

async def main():
    symbol = "btcusdt"
    store = PriceStore(max_length=300)
    plotter = PricePlotter(store)
    alert = AlertManager(price_threshold=65000)
    await track_price(symbol, store, plotter, alert)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🚨 Tracking stopped by user.")
