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
    Contains
    v The vertex in question
    return True if n is in this graph, False otherwise
    """
    def hasVertex(self, v):
        for u in self._vertices:
            if u.id() == v:
                return True
        return False

    """
    An implementation of Dijkstra's Algorithm
    path The paths from s to each vertex
    s The starting vertex
    return The path from s to each vertex
    """
    def findPath(self, path, s):
        bounds = {}
        for v in self._vertices:
            bounds[v.id()] = sys.maxint
        bounds[s.id()] = 0
        pq = Queue.PriorityQueue()

    
    """
    Find a path, if any, between to vertices
    s The starting vertex
    v The ending vertex
    return True if s is connected to v, otherwise False
    """
    def isConnected(self, s, v):
        return
        path = [s]
        if s == v:
            return True
        if not graph.hasVertex(s):
            return False
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
