
from KTrade import Trade

import csv


class TradeReader(object):

    @classmethod
    def _GetStockDicts(cls, filePath):
        ''' Returns a list of dictionaries, one for each trade.
            Expects tab-separated CSV-file (tab-excel) with following columns:
            TradeDate (yyyyMMdd), Transaction (Buy, Sell), Quantity (abs.),
            StockName, Price, Curr, Premium
            Example:
            20141022    Buy    50  TRMO 55,75   SEK   -2 795,00
        '''
        tradeDicts = list()
        fileHandler = open(filePath, 'r')
        tradeDict = dict()
        csvReader = csv.reader(fileHandler, dialect='excel-tab')
        csvReader.next()
        for row in csvReader:
            tradeDict = dict()
            isShort = row[1].startswith('S')
            quantitySign = 1.0-2.0*int(isShort)
            tradeDict['tradeDate'] = '%s-%s-%s' % (row[0][0:4], row[0][4:6], row[0][6:8])
            tradeDict['stockName'] = row[3]
            tradeDict['quantity'] = quantitySign*float(row[2])
            tradeDict['price'] = float(row[4].replace(',', '.').replace(' ', ''))
            # tradeDict['currency'] = row[5]
            tradeDict['premium'] = float(row[6].replace(',', '.').replace(' ', ''))
            tradeDicts.append(tradeDict)
        fileHandler.close()
        return tradeDicts

    @classmethod
    def _TradesFromTradeDicts(cls, tradeDicts):
        ''' Returns a list of trades, given a list of trade dicts. '''
        trades = list()
        for tradeDict in tradeDicts:
            tradeDate = tradeDict.get('tradeDate')
            stockName = tradeDict.get('stockName')
            quantity = tradeDict.get('quantity')
            price = tradeDict.get('price')
            premium = tradeDict.get('premium')
            trade = Trade(tradeDate, stockName, quantity, price, premium)
            trades.append(trade)
        return trades

    @classmethod
    def TradesFromFile(cls, filePath):
        ''' Retrieves the trades in a files. '''
        tradeDicts = cls._GetStockDicts(filePath)
        trades = cls._TradesFromTradeDicts(tradeDicts)
        return trades
