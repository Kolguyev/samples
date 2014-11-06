
class Person(object):

    def __init__(self):
        self.behaviour = None

    def SetBehaviour(self, behaviour):
        self.behaviour = behaviour

    def Move(self):
        if self.behaviour == 'Stressed':
            print 'Running in a hurry.'
        elif self.behaviour == 'Calm':
            print 'Walking calmly.'

    def Talk(self):
        if self.behaviour == 'Stressed':
            print 'Talking quickly and nervously.'
        elif self.behaviour == 'Calm':
            print 'Talking slowly and pleasantly.'


person = Person()

# Stressed behaviour
person.SetBehaviour('Stressed')
print '--- Person is stressed ---'
person.Talk()
person.Move()

# Calm behaviour
person.SetBehaviour('Calm')
print '--- Person is calm ---'
person.Talk()
person.Move()