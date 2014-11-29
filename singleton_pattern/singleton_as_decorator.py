def Singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@Singleton
class SomeClass(object):
  pass


sc1 = SomeClass()
sc2 = SomeClass()

print 1, sc1
print 2, sc2
