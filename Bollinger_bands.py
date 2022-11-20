from backtesting.test import GOOG
from backtesting import Strategy, Backtest
import numpy as np
import pandas_ta as ta


def indicator(data):
    # Data OHLCV
    bbands = ta.bbands(close=data.Close.s, std=2, length=15)
    # print(bbands.to_numpy().T)
    return bbands.to_numpy().T[:3]


class BBStrategy(Strategy):

    def init(self):
        self.bbands = self.I(indicator, self.data)
        # print(self.bbands)
        pass

    def next(self):
        lower_band = self.bbands[0]
        upper_band = self.bbands[2]

        if self.position:
            if self.data.Close[-1] > upper_band[-1]:
                self.position.close()

        else:
            if self.data.Close[-1] < lower_band[-1]:
                self.buy()



bt = Backtest(GOOG, BBStrategy, cash=10_000)
stats = bt.run()
bt.plot()
print(stats)