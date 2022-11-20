from backtesting.test import GOOG
from backtesting.lib import crossover
from backtesting import Strategy
import pandas_ta as ta
from backtesting import Backtest
import yfinance as yf

def spanA(data):
    # Data OHLCV
    ichimoku = ta.ichimoku(data.High.s, data.Low.s, data.Close.s)
    print(ichimoku[0].to_numpy().T)
    return ichimoku[0].to_numpy().T[0]


def spanB(data):
    # Data OHLCV
    ichimoku = ta.ichimoku(data.High.s, data.Low.s, data.Close.s)
    return ichimoku[0].to_numpy().T[1]


def tenkan_Sen(data):
    # Data OHLCV
    ichimoku = ta.ichimoku(data.High.s, data.Low.s, data.Close.s)
    return ichimoku[0].to_numpy().T[2]


def kijun_Sen(data):
    # Data OHLCV
    ichimoku = ta.ichimoku(data.High.s, data.Low.s, data.Close.s)
    return ichimoku[0].to_numpy().T[3]


def chikou_Span(data):
    # Data OHLCV
    ichimoku = ta.ichimoku(data.High.s, data.Low.s, data.Close.s)
    return ichimoku[0].to_numpy().T[4]


class Ichimoku_cross(Strategy):
    # n1 = 20
    # n2 = 25

    def init(self):
        self.span_A = self.I(spanA, self.data)
        self.span_B = self.I(spanB, self.data)
        self.tenkan_sen = self.I(tenkan_Sen, self.data)
        self.kijun_sen = self.I(kijun_Sen, self.data)
        self.chikou_span = self.I(chikou_Span, self.data)


    def next(self):
        if self.position:
            if self.data.Close[-1] < self.kijun_sen[-1] and \
                    self.tenkan_sen[-1] < self.kijun_sen[-1]:
                self.position.close()

        else:
            if self.data.Close[-1] > self.span_A[-1] > self.span_B[-1] and \
                    self.tenkan_sen[-1] > self.kijun_sen[-1] and \
                    self.chikou_span[-1] > self.data.Close[-26]:
                self.buy()


if __name__ == '__main__':
    baba = yf.Ticker("BABA")

    baba_data = baba.history(period='max')

    bt = Backtest(baba_data, Ichimoku_cross, cash=10000, commission=.002,
                  exclusive_orders=True)
    stats = bt.run()
    bt.plot()
    print(stats)
