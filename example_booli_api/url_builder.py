import calendar
import hashlib
import random
from datetime import datetime


class UrlBuilder(object):

    BASESTRING = 'http://api.booli.se'

    def __init__(self):
        self.callerId = None
        self.center = None
        self.dimension = None
        self.freeSearch = None
        self.hash = None
        self.limit = 10
        self.offset = 0
        self.privateKey = None
        self.timeStamp = None
        self.unique = None

    def CallerId(self, callerId=None):
        if callerId == None:
            return self.callerId
        self.callerId = callerId

    def Center(self):
        return self.center

    def Dimension(self):
        return self.dimension

    def OffSet(self, offset=None):
        if offset == None:
            return self.offset
        self.offset = offset

    def PrivateKey(self, privateKey=None):
        if privateKey==None:
            return self.privateKey
        self.privateKey = privateKey

    def SearchType(self):
        return 'sold'

    def SetAreaSearch(self, centerX, centerY, dimension):
        self.center = (centerX, centerY)
        self.dimension = (dimension, dimension)

    def Limit(self, limit=None):
        if limit == None:
            return self.limit
        self.limit = limit

    def TimeStamp(self):
        if self.timeStamp == None:
            self.timeStamp = str(calendar.timegm(datetime.utcnow().timetuple()))
        return self.timeStamp

    def Unique(self):
        if self.unique == None:
            self.unique = ''.join(random.choice('0123456789abcdefgh') for i in range(16))
        return self.unique

    def BaseString(self):
        return self.BASESTRING

    def FreeSearch(self, freeSearch=None):
        if freeSearch == None:
            return self.freeSearch
        self.freeSearch = freeSearch

    def Hash(self):
        if self.hash == None:
            strToHash = ''.join([self.CallerId(),
                                 self.TimeStamp(),
                                 self.PrivateKey(),
                                 self.Unique()])
            s = hashlib.sha1()
            s.update(strToHash)
            self.hash = s.hexdigest()
        return self.hash

    def BuildUrl(self):
        freeText = '' if self.FreeSearch() == None \
            else '&q=' + self.FreeSearch()
        centerAndDimension = '' if self.center == None \
            else '&center='+ '%s,%s' % (str(self.center[0]), str(self.center[1])) \
                 + '&dim=%s,%s' % (str(self.dimension[0]), str(self.dimension[1]))
        return self.BASESTRING + '/' + self.SearchType() + '?' \
            + freeText + '&callerId='+self.CallerId() \
            + '&time='+self.TimeStamp() + '&unique='+self.Unique() \
            + '&hash='+self.Hash() + '&offset='+str(self.OffSet()) \
            + '&limit='+str(self.Limit()) \
            + centerAndDimension \
