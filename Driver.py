from Graph import *
from DatabaseUtils import *

"""
Generate a list of solitary vertices. That is to say, vertices
with empty adjacency lists.
"""
def generateSolitaryV():
    data = {}
    artists = getArtists()
    for a in artists:
        data[a] = Vertex(a, [])
    return data

"""
Populate the given solitary vertices with their appropriate adjacents
data The solitary vertices to be populated with adjacents
return The completed list of vertices
"""
def populateAdjV(data):
    vertices = []
    adj = []
    artists = getArtists()
    for a in artists:
        sim = getSimilarArtists(a)
        for s in sim:
            adj.append(s)
    return vertices
        







if __name__ == '__main__':
    pass
