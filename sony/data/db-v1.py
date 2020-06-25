#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('Sony.db')
# print("Opened database successfully")

# conn.execute('drop table songs')

conn.execute('''create table songs
         (id integer primary key autoincrement,
         folder varchar(128) not null,
         song varchar(64) not null,
         songtype char(3) not null
         )
    ''')
    
print("Table created successfully")

conn.close()