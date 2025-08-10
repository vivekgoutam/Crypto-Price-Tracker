import asyncio
import json
import websockets


async def track_price(symbol, store, plotter, alerts):
    uri = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"

    async with websockets.connect(uri) as websocket:
        print(f"📡 Tracking {symbol.upper()} prices...")
        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                price = float(data['p'])

                store.add_price(price)
                plotter.update_plot()
                alerts.check_price(price)

            except Exception as e:
                print(f"Error: {e}")
                await asyncio.sleep(5)
