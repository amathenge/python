#!/usr/bin/env python

'''
    copy all the songs from allsongs.txt to excel
    path, song
'''

f = open('sonysongs.txt', 'r')
o = open('songs.txt', 'w')

# filename starts at col 37
# extension of file could be ".mp3" or ".m4a"

directory = ''
song = ''
ouputline = False
for line in f:
    line = line.strip()
    if len(line) > len('Directory') and line[:9] == 'Directory':
        directory = line[13:]
        outputline = False
    if len(line) > 4 and line[-4:] in ['.mp3', '.m4a']:
        song = line[36:]
        outputline = True
    else:
        outputline = False
        
    if outputline == True:
        o.write("{}|{}\n".format(directory,song))
        
f.close()
o.close()
