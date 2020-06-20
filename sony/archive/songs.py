#!/usr/bin/env python

# to rename the song, album and title for MP3 songs.
# hi

import taglib
import os, glob

class CEmpty:
    pass

flist = glob.glob("*.mp3")
flist.sort()

for item in flist:
    album = item[:-4]
    try:
        song = taglib.File(item)
        if 'ALBUM' not in song.tags:
            song.tags['ALBUM'] = [album]
        if 'ARTIST' not in song.tags:
            song.tags['ARTIST'] = [album]
        if 'TITLE' not in song.tags:
            song.tags['TITLE'] = [album]
    except:
        song = CEmpty()
        song.tags = {}
        song.tags['ARTIST'] = [album]
        song.tags['ALBUM'] = [album]
        song.tags['TITLE'] = [album]


    # print("\n{}\n".format(item))
    # for k in song.tags:
        # print("{} -> {}".format(k, ', '.join(song.tags[k])))
    # print("\n")
 
    song.tags['ARTIST'] = [album]
    song.tags['ALBUM'] = [album]
    song.tags['TITLE'] = [album]
 
    song.save()

