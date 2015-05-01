from Graph import *
import unittest

# a graph for testing
testGraph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
testV = []
for key, value in testGraph.iteritems():
    adj = []
    for val in value:
        adj.append(Vertex(key, val))
    testV.append(Vertex(key, adj))
    
g = Graph(testV)


"""Test Graph.py"""
class TestGraph(unittest.TestCase):
    
# Vertex ---------------------------------------------------
    """Test id"""
    def test_id(self):
        v = Vertex('A', ['B', 'C'])
        self.assertEqual('A', v.id())

    """Test adj"""
    def test_adj(self):
        v = Vertex('A', ['B', 'C'])
        u = Vertex('A', [v])
        self.assertTrue(v in u.adj())
   
    """Test isAdjacent"""
    def test_isAdjacent(self):
        v = Vertex('A', ['B', 'C'])
        u = Vertex('A', [v])
        self.assertTrue(u.isAdjacent(v))


# Graph ----------------------------------------------------
    """Test printGraph"""
    def test_printGraph(self):
        print ""
        g.printGraph()

    """Test hasVertex"""
    def test_hasVertex(self):
        self.assertTrue(g.hasVertex('A'))
        self.assertFalse(g.hasVertex('U'))

    """Test findPath Valid"""
    def test_findPathValid(self):
        self.assertTrue(g.findPath('A', 'D'))
        
    """Test findPath Invalid"""
    def test_findPathInvalid(self):
        self.assertIsNone(g.findPath('U', 'A'))
        self.assertIsNone(g.findPath('A', 'U'))
