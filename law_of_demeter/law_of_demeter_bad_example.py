

class City(object):

    def __init__(self, name):
        self.name = name

    def Name(self):
        return self.name


class Home(object):

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def Name(self):
        return self.name

    def City(self):
        return self.city


class Person(object):
    
    def __init__(self, name, home):
        self.name = name
        self.home = home

    def Name(self):
        return self.name

    def Home(self):
        return self.home

city = City('Karlstad')
home = Home('Nilssons hemmet', city)
person = Person('Nils', home)

print '%s bor i %s som ligger i staden %s.' % (person.Name(), person.Home().Name(), person.Home().City().Name())
