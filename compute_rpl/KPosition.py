

class Position(object):
    ''' Represents a set of trades on the same stock.
    '''

    def __init__(self, trades):
        self.trades = trades

    def Quantity(self):
        ''' The quantity of the position.'''
        quantity = 0.0
        for trade in self.trades:
            quantity += trade.Quantity()
        return quantity

    def _LongTrades(self):
        return [trade for trade in self.trades if trade.IsLong()]

    def _ShortTrades(self):
        return [trade for trade in self.trades if trade.IsShort()]

    def _AverageLongPrice(self):
        ''' The average price for the long trades.'''
        totalLongPremium = sum([trade.Premium() for trade in self._LongTrades()])
        totalLongQuantity = sum([trade.Quantity() for trade in self._LongTrades()])
        return abs(totalLongPremium/totalLongQuantity)

    def _AverageShortPrice(self):
        ''' The average price for the short trades.'''
        totalShortPremium = sum([trade.Premium() for trade in self._ShortTrades()])
        totalShortQuantity = sum([trade.Quantity() for trade in self._ShortTrades()])
        if not totalShortQuantity:
            return None
        return abs(totalShortPremium/totalShortQuantity)

    def RPL(self):
        ''' Returns Realized Profit and Loss of the position.'''
        longAvgPrice = self._AverageLongPrice()
        shortAvgPrice = self._AverageShortPrice()
        shortQuantity = sum([abs(trade.Quantity()) for trade in self._ShortTrades()])
        if 0.0 in (longAvgPrice, shortAvgPrice, shortQuantity,):
            return 0.0
        return (shortAvgPrice - longAvgPrice)*shortQuantity

