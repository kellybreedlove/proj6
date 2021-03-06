from Driver import *
from DatabaseUtils import *
import unittest

"""Test Driver.py"""
class TestDriver(unittest.TestCase):
        
    """Test generateV"""
    def test_generateV(self):
        expectedAdj = getSimilarArtists("Mastodon")
        
        testVerts = generateV()
        for v in testVerts:
            if v.id() == "Mastodon":
                self.assertTrue(v.adj())
                for a in v.adj():
                    self.assertTrue(a.id() in expectedAdj)
        
    if __name__ == '__main__':
        unittest.main()
