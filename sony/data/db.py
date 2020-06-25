#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('Sony2.db')
# print("Opened database successfully")

# conn.execute('drop table songs')

conn.execute('''create table folders
         (id integer primary key autoincrement,
         folder varchar(128) not null
         )
    ''')
    
conn.execute ('''create table songs
    (id integer primary key autoincrement,
    folder_id integer references folder(id),
    song varchar(64) not null
    
    
print("Table created successfully")

conn.close()