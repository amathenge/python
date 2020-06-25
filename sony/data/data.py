#!/usr/bin/env python

import os
import sqlite3

def get_db():
    sql = sqlite3.connect('sony.db')
    sql.row_factory = sqlite3.Row
    return sql
    
def close_db(db):
    db.close()
    
    
# flist = [ os.path.join(root,i) for root, dirs, files in os.walk('d:\\Sony') for i in files if i[-3:] in ('mp3', 'm4a')]
flist = dict()
for root, dirs, files in os.walk('d:\\Sony'):
    if len(files) > 0:
        flist[root] = files
    
for item in flist.keys():
    print("{} => {}\n\n".format(item, flist[item]))
    
print("There are {} folders with songs\n".format(len(flist)))

# insert them into the database.
# id = primary key - auto generated
# folder = flist->key
# song = flist->value
# songtype = 'MP3' or 'MP4'

for item in flist:
    for song in flist[item]:
        cur = get_db()
        sql = 'insert into songs (folder, song, songtype) values (?, ?, ?)'
        songtype = song[-3:].upper()
        cur.execute(sql, [item, song, songtype])
        cur.commit()
        
print("all done")