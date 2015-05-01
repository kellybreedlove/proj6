from Graph import *
from DatabaseUtils import *
import sys

"""
A class to model data about artist similarty from the MillionSongSubset database as a graph.
Ideally I would extend Graph with ArtistSimilarityGraph.
However, there's some issues with python versions and the use
of super() that I don't quite understand. So, bellow I just make a graph with generateV().

class ArtistSimilarityGraph(Graph):

    def __init__(self):
        super(generateV())
"""

"""
Generate the vertices for the graph.
Do so dynamically, because there is a lot of data.
return A list of the vertices correctly formated create a graph with
"""
def generateV():
    data = {}
    vertices = []
    
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

"""
Main.
Some quickly hacked code for a command line interface into the graph.
"""
if __name__ == '__main__':
    artists = getArtists()

    print ""
    print "Welcome!"
    print "NOTE: your queries will be case sensitive"
    print "Consult the text file graph to get an idea of the artists included in this database"
    print "as well as examples of how artists names are formatted"
    print "Please wait, the graph is loading..."
    
    g = Graph(generateV())
    
    print "loaded."
    print ""
    print "The artist with the most similar artists in this database is: ",
    print g.vertexWithMostAdj()
    print ""
    print "What else would you like to know?"
    print "0 = artists similar to a given artist"
    print "1 = if an artist is connected to another artist through similar artists"
    print "To exit, type 'exit' at any time"

    while True:
        cmnd = raw_input()

        if cmnd == "0":
            cmnd = raw_input("Please specify an artist: ")

            if cmnd in artists:
                print "Similar artists include: "
                sim = g.getAdj(cmnd)
                for s in sim:
                    print s

                print ""
                print "What else would you like to know?"
                print "0 = artists similar to a given artist"
                print "1 = if an artist is connected to another artist through similar artists"
                print "To exit, type 'exit' at any time"               
            else:
                print "I'm sorry, we aren't that hip."
                print "We don't have any information on that artist."
                print "Try another one?"

        elif cmnd == "1":
            cmnd = raw_input("Please specify an artist: ")

            if cmnd in artists:
                
        
            
                print ""
                print "What else would you like to know?"
                print "0 = artists similar to a given artist"
                print "1 = if an artist is connected to another artist through similar artists"
                print "To exit, type 'exit' at any time" 
            else:
                print "I'm sorry, we aren't that hip."
                print "We don't have any information on that artist."
                print "Try another one?"


        elif cmnd == "exit":
            sys.exit()
        else:
            print "Please choose 0, 1, or exit"
        


    
    
        



        
        
        
           
