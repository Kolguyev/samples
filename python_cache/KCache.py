
class Cache(object):

    def __init__(self):
        self.cache = dict()

    def AddValue(self, key, value):
        self.cache[key] = value

    def GetValue(self, key):
        return self.cache.get(key)

    def ClearCache(self):
        self.cache = dict()
