'''
# Example URL:
# http://api.booli.se/sold?&callerId=some_caller_id&time=1416203587&unique=5d0b303g0e3d1125&hash=g77av6re7e81wre12ee7bfd0bf66eeb5e15bda83&offset=0&limit=10&center=59.324564,18.072166&dim=30000.0,30000.0
'''


import unittest

class TestUrlBuilder(unittest.TestCase):

    def setUp(self):
        from url_builder import UrlBuilder
        self.ub = UrlBuilder()
        self.ub.CallerId('some_caller_id')
        self.ub.PrivateKey('somEPrIVATEkEyw8dDdE0WuEmwI9aQqF9N6dTdse')
        self.ub.SetAreaSearch(59.324564, 18.072166, 30000.0)
        self.ub.Limit(10)

    def test_UrlBuilderAttributes(self):
        self.assertEqual(self.ub.BaseString(), 'http://api.booli.se')
        self.assertEqual(self.ub.CallerId(), 'some_caller_id')
        self.assertEqual(self.ub.PrivateKey(), 'somEPrIVATEkEyw8dDdE0WuEmwI9aQqF9N6dTdse')
        self.assertEqual(self.ub.SearchType(), 'sold')
        self.assertEqual(self.ub.OffSet(), 0)
        self.assertEqual(self.ub.Limit(), 10)
        self.assertTrue(1401044813 < int(self.ub.TimeStamp()) < 999999999999)
        self.assertEqual(len(self.ub.Unique()), 16)
        self.assertEqual(type(self.ub.Unique()), str)

    def test_UrlHashString(self):
        import hashlib
        stringToHash = ''.join([self.ub.CallerId(),
                                self.ub.TimeStamp(),
                                self.ub.PrivateKey(),
                                self.ub.Unique()])
        s = hashlib.sha1()
        hashString = s.update(stringToHash).hexdigest()
        self.assertEqual(hashString, self.ub.HashString())
        self.assertEqual(len(self.ub.HashString()), 40)
        self.assertEqual(type(self.ub.HashString()), str)

    def test_BuildQueryString(self):
        urlString = self.ub.BuildUrl()
        self.assertTrue(urlString.startswith('http://api.booli.se/sold?'))
        self.assertTrue('&callerId=some_caller_id' in urlString)
        self.assertTrue('&time=' in urlString)
        self.assertTrue('&unique=' in urlString)
        self.assertTrue('&hash=' in urlString)
        self.assertTrue('&offset=0' in urlString)
        self.assertTrue('&limit=10' in urlString)
        self.assertTrue('&center=59.324564,18.072166' in urlString)
        self.assertTrue('&dim=30000,30000' in urlString)

unittest.main()