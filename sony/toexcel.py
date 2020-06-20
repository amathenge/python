#!/usr/bin/env python

# copy files from songlen.txt to csv format for excel

f = open('sonysongs.txt','r')
o = open('songs.txt', 'w')

cont = True
counter = 0

sname = f.readline().strip()
slen = f.readline().strip().split()
slen = slen[1]
stitle = f.readline().strip()
dummy = f.readline()

while cont:
    counter += 1
    o.write("{}|{}|{}\n".format(slen,sname,stitle))
    
    sname = f.readline().strip()
    slen = f.readline().strip().split()
    if len(slen) > 1:
        slen = slen[1]
    stitle = f.readline().strip()
    dummy = f.readline()

    if sname == "":
        cont = False
        
    if counter % 10 == 0:
        print(".", end='')
    if counter % 100 == 0:
        print("")
    if counter > 2500:
        cont = False
        
f.close()
o.close()
