import pandas as pd
from backtesting.lib import crossover
from backtesting import Backtest, Strategy
from backtesting.test import SMA


class Sma_cross(Strategy):
    n1 = 20
    n2 = 25

    def init(self):
        # super().init()
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


