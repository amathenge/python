#!/usr/bin/env python

'''
    song shuffler.

'''

import random

f = open('soft.m3u','r')
o = open('softlist.m3u','w')

items = []

# discard header.
f.readline()
counter = 0
for song in f:
    counter += 1
    
songcount = counter // 2

while counter > 0:
    items.append(counter)
    counter -= 1
    
# display

print("{}".format(items))

random.shuffle(items)

print("{}".format(items))

o.write('#EXTM3U\n')
counter = 0
song = 0
head = ''
title = ''
while counter < len(items):
    f.seek(0)
    f.readline()
    song = items[counter]
    while song > 0:
        head = f.readline()
        title = f.readline()
        song -= 1
    o.write("{}{}".format(head,title))
    
    counter += 1
 
f.close()
o.close()
