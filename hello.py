#!/usr/bin/env python

print("Hello World")

for item in range(1,11):
    print(item,sep='\n')

a = ()
a += ('one',)
print("the value of the tuple is {}".format(a[0]))

# dictionaries in Python

d = {}
for x in range(1,101):
    y = str(x)
    d[y] = x

print("dict {}".format(d))

# dictionaries are mutable.
# tuples (lists) are not mutable = immutable

# opening files
