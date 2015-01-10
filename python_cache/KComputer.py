
from KCache import Cache


class Computer(object):

    def __init__(self):
        self.cache = Cache()

    def ClearCache(self):
        self.cache.ClearCache()

    def Compute(self, base, exponent):
        # Create key as tuple
        key = (base, exponent)

        # Retrieve value from cache (if any)
        cachedValue = self.cache.GetValue(key)
        if cachedValue != None:
            print 'Key %s found in cache (value = %.0f).' % (str(key), cachedValue)
            return cachedValue

        # Compute value and put in cache
        value = base**exponent
        print '<Computing: %.0f^%.0f = %.0f>' % (base, exponent, value)
        self.cache.AddValue(key, value)
        print 'Added key %s to cache (value = %.0f).' % (str(key), value)
        return value

