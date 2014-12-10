

class Trade(object):
    ''' Representation of a trade on a stock.
    '''

    def __init__(self, tradeDate, stockName, quantity, price, premium=None):
        self.tradeDate = tradeDate
        self.stockName = stockName
        self.quantity = quantity
        self.price = price
        self.premium = premium

    def TradeDate(self):
        return self.tradeDate

    def StockName(self):
        return self.stockName

    def Quantity(self):
        return self.quantity

    def Price(self):
        return self.price

    def Premium(self):
        ''' Returns the premium if given, otherwise computes it. '''
        if self.premium != None:
            return self.premium
        return -self.quantity*self.price

    def IsLong(self):
        return self.quantity > 0

    def IsShort(self):
        return self.quantity < 0

