import sqlite3
from Graph import *
"""
A utility class with useful functions for data retrieval from the
MillionSongSubset SQLite3 database.
"""


"""
Run the given SQL command
(Compliments of aaronasterling on stack overflow).
Untested & unused, but it seems like a nice idea.
"""                   
def runCommand(cmd, params=(), commit=False):
    c.execute(cmd, params)
    if commit:
        conn.commit()

"""
Get a list of the artists in this database.
return The alphabetical list of artists in this database
"""
def getArtists():
    conn = sqlite3.connect('subset_track_metadata.db')
    c = conn.cursor()    
    with conn:
        cmd = "select artist_name from songs"
        c.execute(cmd)

        rawA = set() # so no duplicates
        raw = c.fetchall()
        for row in raw:
            rawA.add(row)

        # move it to a list because they're easier to work with and sortable
        artists = [i[0] for i in raw]
        artists.sort()
        
        return artists
        
"""
Get the artist that correpsonds to the given ID.
id The ID of the artist to retrieve
return The slightly man handled string that is the name of the artist in question
"""
def idToArtist(id):
    conn = sqlite3.connect('subset_track_metadata.db')
    c = conn.cursor()   
    with conn:
        cmd = "select artist_name from songs where songs.artist_id = ?"
        params = (id, )
        c.execute(cmd, params)

        artist = []
        raw = c.fetchall()
        for row in raw: artist.append(row)

        if artist:
            return artist[0][0]

"""
Get the ID that corresponds to the given artist.
artist The artist to retrieve the ID for
return The slightly man handled string that is the ID of the artist in question
"""
def artistToID(artist):
    conn = sqlite3.connect('subset_track_metadata.db')
    c = conn.cursor()
    with conn:
        cmd = "select artist_id from songs where songs.artist_name = ?"
        params = (artist, )
        c.execute(cmd, params)

        artist = [] 
        raw = c.fetchall()
        for row in raw: artist.append(row)

        if artist:
            return artist[0][0]
    
"""
Get all artists that are listed as being similar to the given artist.
artist The artist in question.
return The alphabetical list of all artists similar to the one in question
"""
def getSimilarArtists(artist):
    artistID = artistToID(artist) # None ?
    
    conn = sqlite3.connect('subset_artist_similarity.db')
    c = conn.cursor()
    with conn:
        cmd = "select similar from similarity where similarity.target = ?"
        params = (artistID, )
        c.execute(cmd, params)

        rawA = set() # so no duplicates
        raw = c.fetchall()
        for row in raw:
            rawA.add(row)

        # move it to a list because they're easier to work with and sortable
        artists = [idToArtist(i[0]) for i in raw]
        artists.sort()
    
        return artists

if __name__ == "__main__":
    sim = getSimilarArtists("Mastodon")
    for a in sim: print a
        
