from TAcharts.indicators.ichimoku import Ichimoku
from backtesting.test import GOOG


if __name__ == '__main__':
    df = GOOG[:1000]
    df['Date'] = df.index
    df.reset_index(drop=True, inplace=True)

    i = Ichimoku(df)
    i.build(20, 60, 120, 30)
    i.plot()

