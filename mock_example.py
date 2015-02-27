
class FileReader(object):

	def __init__(self, filePath):
		self.filePath = filePath

	def GetContent(self):
		fileHandle = open(self.filePath, 'r')
		content = fileHandle.read()
		fileHandle.close()
		return content


import unittest
from mock import Mock, patch

class TestFileReader(unittest.TestCase):

	def test_GetContent(self):
		mockFileHandle = Mock()
		mockFileHandle.read.return_value = 'Some text in a file..'
		with patch('__builtin__.open', return_value=mockFileHandle):
			fileReader = FileReader('some_file.txt')
			content = fileReader.GetContent()
			self.assertEqual(content, 'Some text in a file..')
			self.assertTrue(mockFileHandle.read.called)
			self.assertTrue(mockFileHandle.close.called)
			self.assertEqual(open.call_args[0], ('some_file.txt', 'r'))


unittest.main()
