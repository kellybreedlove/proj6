from TestGraph import *
from TestDatabaseUtils import *
from TestDriver import *
import unittest

testSuite = unittest.makeSuite(TestGraph)
testSuite.addTest(unittest.makeSuite(TestDatabaseUtils))
testSuite.addTest(unittest.makeSuite(TestDriver))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
