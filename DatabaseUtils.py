import sqlite3
from Graph import *

"""
Run the given SQL command
(Compliments of aaronasterling on stack overflow).

"""                   
def runCommand(cmd, params=(), commit=False):
    c.execute(cmd, params)
    if commit:
        conn.commit()

"""
Get the artist that correpsonds to the given ID.
id The ID of the artist to retrieve
return The slightly man handled string that is the artist in question's name
"""
def getArtistFromID(id):
    conn = sqlite3.connect('subset_track_metadata.db')
    c = conn.cursor()
    
    with conn:
        cmd = "ATTACH DATABASE ? as ?"
        c.execute(cmd, ('subset_artist_similarity.db', 'db'))

        cmd = "select artist_name from songs join db.similarity on similarity.target = songs.artist_id where similarity.target = ?"
        c.execute(cmd, (id, ))

        artist = set() # so no duplicates
        rows = c.fetchall()
        for row in rows: artist.add(row)
        toReturn = next(iter(artist))
            
        return toReturn[0]

"""
"""



    

if __name__ == "__main__":
    print getArtistFromID("ARMQHX71187B9890D3")
