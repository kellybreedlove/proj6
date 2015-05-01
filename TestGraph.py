from Graph import *
import unittest

# a graph for testing
testGraph = {'A': ['B', 'C', 'F'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

data = {}
testV = []
for key, value in testGraph.iteritems():

    # get/create the vertex for this artist
    if not key in data:
        data[key] = Vertex(key, [])
    v = data[key]

    # add its adjacents
    for val in value:
        if not val in data:
            data[val] = Vertex(val, [])
        v.addAdj(data[val])
    
    # add it to the list of vertices   
    testV.append(v)
    
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

    """Test addAdj"""
    def test_addAdj(self):
        v = Vertex('A', ['B', 'C'])
        u = Vertex('A', [])
        v.addAdj(u)
        self.assertTrue(u in v.adj())
        
        
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

    """Test getV"""
    def test_getV(self):
        v = Vertex('A', [])
        self.assertEqual('A', v.id())

    """Test hasVertex"""
    def test_hasVertex(self):
        self.assertTrue(g.hasVertex('A'))
        self.assertFalse(g.hasVertex('U'))

    """Test getAdj"""
    def test_getAdj(self):
        adj = ['B', 'C', 'F']
        self.assertEqual(adj, g.getAdj('A'))

    """Test vertexWithMostAdj"""
    def test_vertexWithMostAdj(self):
        self.assertEqual('A', g.vertexWithMostAdj())

        
    """Test findPath Valid"""
    def test_findPathValid(self):
        path = ['A', 'C', 'D']
        self.assertTrue(g.findPath('A', 'D'))
        self.assertEqual(path, g.findPath('A', 'D'))
        
    """Test findPath Invalid"""
    def test_findPathInvalid(self):
        null = ["These artists are not connected"]
        self.assertEqual(null, g.findPath('U', 'A'))
        self.assertEqual(null, g.findPath('A', 'U'))

    if __name__ == '__main__':
        unittest.main()
