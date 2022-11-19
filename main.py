from SMA_CROSS import Sma_cross
from backtesting import Backtest
from backtesting.test import GOOG
import pandas as pd


if __name__ == '__main__':
    bt = Backtest(GOOG, Sma_cross, cash=10000, commission=.002,
                  exclusive_orders=True)

    output = bt.run()
    bt.plot()
    print(output)