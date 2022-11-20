from SMA_CROSS import Sma_cross
from backtesting import Backtest
from backtesting.test import GOOG
import pandas as pd
from Ichimoku import Ichimoku_cross


if __name__ == '__main__':
    bt = Backtest(GOOG, Ichimoku_cross, cash=10000, commission=.002,
                  exclusive_orders=True)

    stats = bt.run()
    # bt.plot()
    print(stats)