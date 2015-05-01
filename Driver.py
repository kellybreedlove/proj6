aquimport sqlite3
from Graph import *

def musicV():
    conn1 = sqlite3.connect('subset_artist_term.db')
    conn2 = sqlite3.connect('subset_artist_similarity.db')
    conn3 = sqlite3.connect('subset_track_metadata.db')
    
    with conn:    
        
        c = conn.cursor()    
        c.execute('select * from artists')
        
        rows = c.fetchall()
        for row in rows:
            print row

if __name__ == '__main__':
    g = Graph(musicV())
    g.printGraph()

