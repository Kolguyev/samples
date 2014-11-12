# Market
class Publisher(object):

    def __init__(self, name):
        self.name = name
        self.subscribers = list()

    def Name(self):
        return self.name

    def AddSubscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
        print '%s started subscription to %s.' % (subscriber.Name(), self.Name())

    def RemoveSubscriber(self, subscriber):
        self.subscribers.remove(subscriber)
        print '%s ended subscription to %s.' % (subscriber.Name(), self.Name())

    def PublishStockPriceUpdate(self, stockPrice):
        print '--- %s published updated stock price: %.2f. ---' % (self.Name(), stockPrice)
        for subscriber in self.subscribers:
            # Notify subscribers about update
            subscriber.PublishedStockPrice(stockPrice)

# Trader
class Subscriber(object):

    def __init__(self, name):
        self.name = name

    def Name(self):
        return self.name

    def Subscribe(self, publisher):
        publisher.AddSubscriber(self)

    def StopSubscription(self, publisher):
        publisher.RemoveSubscriber(self)

    def PublishedStockPrice(self, stockPrice):
        print '%s was notified about the updated stock price %.2f.' % (self.Name(), stockPrice)


# Init
publisher = Publisher('OMX Market')
trader1 = Subscriber('STAL Invest trader')
trader2 = Subscriber('Berida Bank trader')
trader3 = Subscriber('HedgeFive trader')

# Start subscriptions
trader1.Subscribe(publisher)
trader2.Subscribe(publisher)
trader3.Subscribe(publisher)

# First price update
publisher.PublishStockPriceUpdate(55.8)

# Trader cancels subscriptions
trader2.StopSubscription(publisher)

# Second price update
publisher.PublishStockPriceUpdate(56.1)