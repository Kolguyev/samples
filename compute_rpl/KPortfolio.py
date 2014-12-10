
from KPosition import Position


class Portfolio(object):
    ''' Representation of a portfolio. Holds a list of trades,
        that can be aggregated into positions (grouped by
        stock).
    '''

    def __init__(self, trades):
        self.trades = trades

    def Trades(self):
        return self.trades

    def StockNames(self):
        stockNames = list()
        for trade in self.trades:
            if trade.StockName() not in stockNames:
                stockNames.append(trade.StockName())
        return stockNames

    def TradesInStock(self, stockName):
        trades = list()
        for trade in self.trades:
            if trade.StockName() in (stockName,):
                trades.append(trade)
        return trades

    def PositionByStockName(self, stockName):
        positionTrades = list()
        for trade in self.trades:
            if trade.StockName() in (stockName,):
                positionTrades.append(trade)
        return Position(positionTrades)

    def RPL(self):
        totalRPL = 0.0
        for stockName in self.StockNames():
            position = self.PositionByStockName(stockName)
            totalRPL += position.RPL()
        return totalRPL
