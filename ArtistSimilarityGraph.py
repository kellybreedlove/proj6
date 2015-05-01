from Graph import *
from DatabaseUtils import *

"""
A class to model data about artist similarty from the MillionSongSubset database as a graph.
"""
class ArtistSimilarityGraph(Graph):

    def __init__(self):
        super(generateV())       

"""
Generate the vertices for the graph.
Do so dynamically, because there is a lot of data.
return A list of the vertices correctly formated create a graph with
"""
def generateV():
    data = {}
    vertices = []
    adj = []
    
    artists = getArtists()
    for a in artists:

        # get/create the vertex for this artist
        if not a in data:
            data[a] = Vertex(a, [])
        v = data[a]

        # add its adjacents
        sim = getSimilarArtists(a)
        for s in sim:
            if not s in data:
                data[s] = Vertex(s, [])
            v.addAdj(data[s])

        # add it to the list of vertices
        vertices.append(v)
            
    return vertices

if __name__ == '__main__':
    g = ArtistSimilarityGraph()
    g.printGraph()
    


    
