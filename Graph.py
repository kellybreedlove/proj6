import sys
import Queue

"""
A class to model a vertex in a graph.
"""
class Vertex(object):

    """
    idVal The id or value stored at this vertex 
    adjs The vertices that are adjacent to this vertex
    """
    def __init__(self, idVal, adjs):
        self._id = idVal
        self._adjacents = adjs
       
    """
    An accessor for this vertex's id
    """
    def id(self):
        return self._id

    """
    An accessor for this vertex's adjacent vertices
    """
    def adj(self):
        return self._adjacents

    """
    A mutator for this vertex's adjacent vertices
    """
    def addAdj(self, adj):
        self._adjacents += [adj]
        
    """
    A contains method for adjacents
    v The vertex in question
    """
    def isAdjacent(self, v):
        for u in self._adjacents:
            if u.id() == v.id():
                return True
        return False


"""
A class to model a graph.
"""
class Graph(object):

    """
    v All of the vertices in this graph
    """
    def __init__(self, v):
        self._vertices = v

    """
    Print this graph
    """
    def printGraph(self):
        for v in self._vertices:
            for a in v.adj():
                print "%s -> %s" % (v.id(), a.id())

    """
    "Private" Helper
    Find the vertex that corresponds to the given id
    return The vertex object that corresponds to the given id
    """
    def getV(self, v):
        for u in self._vertices:
            if u.id() == v:
                return u
        return None
                  
    """
    Contains
    v The id of the vertex in question
    return True if n is in this graph, False otherwise
    """
    def hasVertex(self, v):
        for u in self._vertices:
            if u.id() == v:
                return True
        return False

    """
    Find the adjacent vertices to this vertex in the graph
    return The id of adjacent vertices
    """
    def getAdj(self, v):
        raw = set()
        for u in self._vertices:
            if u.id() == v:
                for a in u.adj():
                    raw.add(a.id())
                adj = [i for i in raw]
                adj.sort()
                return adj
        return ["None"]
        
    """
    Find the vertex with the most adjacent vertices in this graph
    return The id of vertex with the most adjacent vertices
    """
    def vertexWithMostAdj(self):
        maxAdj = self._vertices[0]
        for v in self._vertices:
            if len(v.adj()) > len(maxAdj.adj()):
                maxAdj = v
        return maxAdj.id()
    
    """
    Find a path, if any, from vertex s to vertex v in this graph.
    Do so using depth first search.
    path The paths from s to each vertex
    s The id of the starting vertex
    v The id of the ending vertex
    return The path from s to v
    """
    def findPath(self, sID, vID):
        if not g.hasVertex(sID) or not g.hasVertex(vID):
            return None

        s = getV(sID)
        v = getV(vID)

        info = {}
        info

        
        
        
        
