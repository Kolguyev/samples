
import unittest

from KTrade import Trade


class TestTrade(unittest.TestCase):

    def setUp(self):
        pass

    def test_InitializeTrade(self):
        trade = Trade('2014-06-05', 'ERIC A', 100.0, 54.3)
        self.assertNotEqual(trade, None)
        self.assertEqual(trade.TradeDate(), '2014-06-05')
        self.assertEqual(trade.StockName(), 'ERIC A')
        self.assertEqual(trade.Quantity(), 100.0)
        self.assertEqual(trade.Price(), 54.3)
        self.assertEqual(trade.Premium(), -5430.0)

    def test_LongShortTrades(self):
        longTrade = Trade('2014-06-05', 'ERIC A', 100.0, 54.3)
        self.assertTrue(longTrade.IsLong())
        self.assertFalse(longTrade.IsShort())
        shortTrade = Trade('2014-06-05', 'ERIC A', -100.0, 54.3)
        self.assertTrue(shortTrade.IsShort())
        self.assertFalse(shortTrade.IsLong())


class TestPosition(unittest.TestCase):


    def test_InitializePosition(self):
        from KPosition import Position
        from KTrade import Trade
        trades = [
            Trade('2014-06-05', 'ERIC A', 100.0, 54.3),
            Trade('2014-06-05', 'ERIC A', 150.0, 57.3),
            Trade('2014-06-05', 'ERIC A', -50.0, 60.2),
        ]
        position = Position(trades)
        self.assertEqual(position.Quantity(), 200.0)

    def test_PositionRPL(self):
        from KPosition import Position
        from KTrade import Trade
        trades = [
            Trade('2014-06-05', 'ERIC A', 100.0, 54.3),
            Trade('2014-07-01', 'ERIC A', -50.0, 64.3),
        ]
        position = Position(trades)
        self.assertNotEqual(position, None)
        self.assertEqual(position.Quantity(), 50)
        self.assertEqual(position.RPL(), 500)


class TestPortfolio(unittest.TestCase):

    def test_InitializePortfolio(self):
        from KPortfolio import Portfolio
        from KTrade import Trade
        trades = [
            Trade('2014-06-05', 'ERIC A', 100.0, 54.3),
            Trade('2014-06-05', 'ERIC A', 150.0, 57.3),
            Trade('2014-06-05', 'ERIC A', -50.0, 60.2),
            Trade('2014-06-05', 'INVE B', 75.0, 280.1),
        ]
        portfolio = Portfolio(trades)
        self.assertEqual(len(portfolio.Trades()), 4)
        self.assertEqual(len(portfolio.StockNames()), 2)
        self.assertTrue('ERIC A' in portfolio.StockNames())
        self.assertTrue('INVE B' in portfolio.StockNames())
        self.assertEqual(len(portfolio.TradesInStock('ERIC A')), 3)

    def test_StocksInPortfolio(self):
        from KPortfolio import Portfolio
        from KTrade import Trade
        trades = [
            Trade('2014-06-05', 'ERIC A', 100.0, 54.3),
            Trade('2014-06-05', 'ERIC A', 150.0, 57.3),
            Trade('2014-06-05', 'SEB A', -50.0, 60.2),
            Trade('2014-06-05', 'INVE B', 75.0, 280.1),
        ]
        portfolio = Portfolio(trades)
        self.assertEqual(len(portfolio.StockNames()), 3)
        self.assertTrue('ERIC A' in portfolio.StockNames())
        self.assertTrue('SEB A' in portfolio.StockNames())
        self.assertTrue('INVE B' in portfolio.StockNames())

    def test_RPLOfZeroPositionWithDefinedTradePremiums(self):
        from KPortfolio import Portfolio
        from KTrade import Trade
        trades = [
            Trade('2014-06-05', 'ERIC A', 100.0, 50.0, -5009.0),
            Trade('2014-06-06', 'ERIC A', -100.0, 50.0, 4991.0),
        ]
        portfolio = Portfolio(trades)
        position = portfolio.PositionByStockName('ERIC A')
        self.assertEqual(position.Quantity(), 0.0)
        self.assertAlmostEqual(position.RPL(), -18.0)


unittest.main()
