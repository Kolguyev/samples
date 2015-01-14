

class SalesmanInteractions(object):
    ''' A Mediator class, responsible for the interactions
        between Salesmen.
    '''

    def __init__(self, subject):
        self.subject = subject

    def BuyItem(self, buyer, seller, item, price):
        buyer.RemoveMoney(price)
        seller.AddMoney(price)
        seller.RemoveItem(item)
        buyer.AddItem(item)

    # (more methods related to interactions could be defined here)


class Salesman(object):
    ''' Represents a sales man, capable of buying and
        possessing money and items.
    '''
    def __init__(self, name):
        self.name = name
        self.items = list()
        self.money = 0.0
        self.interactions = SalesmanInteractions(self)

    def Name(self):
        return self.name

    def Items(self):
        return self.items

    def AddItem(self, item):
        self.items.append(item)

    def RemoveItem(self, item):
        self.items.remove(item)

    def Money(self):
        return self.money

    def AddMoney(self, amount):
        self.money += amount

    def RemoveMoney(self, amount):
        self.money -= amount

    def BuyItem(self, seller, item, price):
        self.interactions.BuyItem(self, seller, item, price)
        print 'Event: %s buys %s from %s at price %.2f.' % (buyer.Name(), item, seller.Name(), price)


# Example of using the classes

def PrintStatus(buyer, seller):
    print '%s items:' % buyer.Name(), buyer.Items()
    print '%s money:' % buyer.Name(), buyer.Money()

    print '%s items:' % seller.Name(), seller.Items()
    print '%s money:' % seller.Name(), seller.Money()

seller = Salesman('Seller')
seller.AddItem('a loaf of bread')

buyer = Salesman('Buyer')
buyer.AddMoney(500.0)

print '--- Status (before trade) ---'
PrintStatus(buyer, seller)

# Make trade
buyer.BuyItem(seller, 'a loaf of bread', 30.0)

print '--- Status (after trade) ---'
PrintStatus(buyer, seller)

