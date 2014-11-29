
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance


class FileHandler(Singleton):
    # Class variables
    filePath = r'C:\temp\myfile.txt'
    content = None

    def __init__(self):
        pass

    def ReadContentFromFile(self):
        # Return content of file
        fileHandle = open(self.filePath, 'r')
        content = fileHandle.read()
        fileHandle.close
        print 'Read file %s.' % self.filePath
        return content

    def GetContent(self):
        if not self.content:
            self.content = self.ReadContentFromFile()
        return self.content


# First instance reads content
fh1 = FileHandler()
content = fh1.GetContent()
print 'First instance gets content:', content

# Second (same) instance gets (already read) content
print ''
fh2 = FileHandler()
content = fh2.GetContent()
print 'Second instance gets content:', content
