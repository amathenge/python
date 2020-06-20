#!/usr/bin/env python

import os
# the taglib library needs to be installed = pip install pytaglib
import taglib

class CEmpty:
    pass

flist = [os.path.join(root,i) for root, dirs, files in os.walk('D:\\MUSIC') for i in files if i[-3:] in ('mp3','m4a')]

o = open('sonysongs.txt','w')
counter = 0

for item in flist:
    counter += 1
    song_length = 0
    album = item[item.rfind('\\')+1:][:-4]
    if album[len(album)-4] == '.':
        album = album[:-4]
        
    try:
        song = taglib.File(item)
        song_length = song.length
        if 'ALBUM' not in song.tags:
            song.tags['ALBUM'] = [album]
        if 'ARTIST' not in song.tags:
            song.tags['ARTIST'] = [album]
        if 'TITLE' not in song.tags:
            song.tags['TITLE'] = [album]
    
        song_info = song.tags['ARTIST'][0] + ' - ' + song.tags['TITLE'][0]
    except:
        song = CEmpty()
        song.tags = {}
        song.tags['ARTIST'] = [album]
        song.tags['ALBUM'] = [album]
        song.tags['TITLE'] = [album]
        
        song_info = song.tags['ARTIST'][0]

    
    try:   
        o.write("{}\n".format(item))
        o.write("len:{:6d}\n".format(song_length))
        o.write("{}\n".format(song_info))
        o.write(">\n")
        print("item: {} len: {:6d} song: {}".format(counter, song_length, song_info))
    except:
        print("error at song {}".format(counter))
    
o.close()
