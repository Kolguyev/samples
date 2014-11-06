
class CalmStrategy(object):

    def Move(self):
        print 'Walking calmly.'

    def Talk(self):
        print 'Talking slowly and pleasantly.'

class StressedStrategy(object):

    def Move(self):
        print 'Running in a hurry.'

    def Talk(self):
        print 'Talking quickly and nervously.'


class Person(object):

    def __init__(self):
        self.strategy = None

    def SetBehaviour(self, strategy):
        self.strategy = strategy

    def Move(self):
        self.strategy.Move()

    def Talk(self):
        self.strategy.Talk()


person = Person()

# Stressed behaviour
print '--- Changing strategy to stressed ---'
person.SetBehaviour(StressedStrategy())
person.Talk()
person.Move()

# Calm behaviour
print '--- Changing strategy to calm ---'
person.SetBehaviour(CalmStrategy())
person.Talk()
person.Move()