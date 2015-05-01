import sys
import Queue

"""
A class to model a vertex in a graph.
"""
class Vertex:

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
    This will overwrite all adjacents and is used only when
    generating the initial vertices. It's a necessary evil for now.
    """
    def setAdj(self, adj):
        self._adjacents = adj
        
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
class Graph:

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
    Find a path, if any, from vertex s to vertex v in this graph.
    path The paths from s to each vertex
    s The starting vertex
    return The path from s to each vertex
    """
    def findPath(self, s, v, path = []):
        path += [s]
        if s == v:
            return path
        if not self.hasVertex(s) or not self.hasVertex(v):
            return None
        for u in self._vertices:
            if u not in path:
                newpath = self.findPath(u, v, path)
                if newpath: return newpath
            
    """
    Find the minimum spanning tree of this graph
    return The minimum spanning tree
    """
    def minSpanningTree(self):
        pass

    
