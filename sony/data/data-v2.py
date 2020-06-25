#!/usr/bin/env python

import os

# flist = [ os.path.join(root,i) for root, dirs, files in os.walk('d:/Sony') for i in files if i[-3:] in ('mp3', 'm4a')]
dlist = [ os.path.join(root,i) for root, dirs, files in os.walk('d:/Sony') for i in dirs ]
# fcount = len(flist)

fcount = 0
totMP3 = 0
totM4A = 0
strMostSongs = ''
iMostSongs = 0

for item in dlist:
    flist = [ os.path.join(root, i) for root, dirs, files in os.walk(item) for i in files if i[-3:] in ('mp3', 'm4a') ]
    m3list = [ os.path.join(root, i) for root, dirs, files in os.walk(item) for i in files if i[-3:] in ('mp3') ]
    totMP3 += len(m3list)
    m4list = [ os.path.join(root, i) for root, dirs, files in os.walk(item) for i in files if i[-3:] in ('m4a') ]
    totM4A += len(m4list)
    print("{:4d} files => {}".format(len(flist), item))
    print("{:8d} mp3's".format(len(m3list)))
    print("{:8d} m4a's".format(len(m4list)))
    if len(flist) > iMostSongs:
        iMostSongs = len(flist)
        strMostSongs = item
    
print("{:6d} Total MP3's".format(totMP3))
print("{:6d} Total M4A's".format(totM4A))
print("\n{} songs in {}".format(iMostSongs, strMostSongs))


