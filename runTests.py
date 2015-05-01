from TestGraph import *
from TestDatabaseUtils import *
import unittest

testSuite = unittest.makeSuite(TestGraph)
testSuite.addTest(unittest.makeSuite(TestDatabaseUtils))

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
