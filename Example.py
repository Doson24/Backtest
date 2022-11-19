from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import talib

print(GOOG)

class RsiOscillator(Strategy):
    
    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, 14)


    def next(self):
        pass

if __name__ == '__main__':
    pass

    # print(talib.)