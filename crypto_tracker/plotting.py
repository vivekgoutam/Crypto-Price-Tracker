import matplotlib.pyplot as plt
import pandas as pd

class PricePlotter:
    def __init__(self, store):
        self.store = store
        plt.ion()
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], label='Price')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Price (USD)')
        self.ax.legend()

    def update_plot(self):
        df = self.store.get_dataframe()
        if not df.empty:
            self.line.set_xdata(range(len(df)))
            self.line.set_ydata(df['price'])
            self.ax.relim()
            self.ax.autoscale_view()
            plt.draw()
            plt.pause(0.01)

