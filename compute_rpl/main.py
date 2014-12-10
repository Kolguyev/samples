from KTrade import Trade
from KTradeReader import TradeReader
from KPortfolio import Portfolio


class ResultsViewer(object):
    ''' Responsible for presenting the results.
    '''

    def __init__(self, filePath):
        self.filePath = filePath

    def PrintPortfolioInformation(self):
        trades = TradeReader.TradesFromFile(self.filePath)
        portfolio = Portfolio(trades)

        print '{0:15}{1:17}{2:25}'.format('Stock', 'Quantity', 'RPL')
        print 40*'-'
        for stockName in portfolio.StockNames():
            position = portfolio.PositionByStockName(stockName)
            print '{0:10}{1:10}{2:15}'.format(stockName, int(position.Quantity()), int(position.RPL()))
        print 40*'-'
        print 'Total RPL: {0:15}{1:10}'.format('', int(portfolio.RPL()))


viewer = ResultsViewer('trades.csv')
viewer.PrintPortfolioInformation()