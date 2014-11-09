import ConfigParser

# Read config file
config = ConfigParser.RawConfigParser()
config.read('example.cfg')

print 'Options and values:'
for option in config.options('General'):
    print "%s: %s" % (option, config.get('General', option))

callerId = config.get('General', 'caller_id')
enabled = config.getboolean('General', 'enabled')

print '\nCaller Id (from config file):', callerId
print '\nAccount enabled:', enabled

