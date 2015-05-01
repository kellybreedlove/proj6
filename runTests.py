from TestGraph import *
from TestDatabaseUtils import *
from TestArtistSimilarityGraph import *
import unittest

testSuite = unittest.makeSuite(TestGraph)
testSuite.addTest(unittest.makeSuite(TestDatabaseUtils))
testSuite.addTest(unittest.makeSuite(TestArtistSimilarityGraph))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
