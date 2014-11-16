
def Memoize(func):
    memo = dict()
    def Func(key):
        if key not in memo:
            # Store if not already stored
            memo[key] = func(key)
        else:
            # If stored
            print '<Retrieving value from cache for %s: %s>' % (str(key), str(memo[key]))
        return memo[key]
    return Func


@Memoize
def CalculateSquare(number):
    print 'Calculating %d squared...' % number
    return number ** 2

print 'Now making first calculation..'
result = CalculateSquare(5)
print 'Result of calculation:', result
print 'Now making second calculation..'
result = CalculateSquare(5)
print 'Result, second calculation:', result
