

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

    def CityName(self):
        return self.city.Name()


class Person(object):
    
    def __init__(self, name, home):
        self.name = name
        self.home = home

    def Name(self):
        return self.name

    def HomeName(self):
        return self.home.Name()

    def CityName(self):
        return self.home.CityName()

city = City('Karlstad')
home = Home('Nilssons hemmet', city)
person = Person('Nils', home)

print '%s bor i %s som ligger i staden %s.' % (person.Name(), person.HomeName(), person.CityName())
