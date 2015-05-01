from TestGraph import *
import unittest

testSuite = unittest.makeSuite(TestGraph)
#testSuite.addTest(unittest.makeSuite())

testRunner = unittest.TextTestRunner()
testRunner.run(testSuite)
