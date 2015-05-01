from DatabaseUtils import *
import unittest

"""
Test DatabaseUtils.py
In the spirit of Wheaton, the tests are all done with queries about
the band Mastodon. Less in the spirit of Wheaton, Mastodon is a
heavy metal band with albums such as Leviathan and Blood Mountain.
"""
class TestDatabaseUtils(unittest.TestCase):

    """Test getArtists"""
    def test_getArtists(self):
        artists = getArtists()
        self.assertTrue(artists) # True if not empty / don't crash
        self.assertTrue("Mastodon" in artists)
        
    """Test idToArtist"""
    def test_idToArtist(self):
        self.assertEqual("Mastodon", idToArtist("ARMQHX71187B9890D3"))

    """Test artistToID"""
    def test_artistToID(self):
        self.assertEqual("ARMQHX71187B9890D3", artistToID("Mastodon"))

    """Test getSimilarArtists"""
    def test_getSimliarArtists(self):
        artists = getSimilarArtists("Mastodon")
        self.assertTrue(artists) # True if not empty / don't crash
                
    if __name__ == '__main__':
        unittest.main()
