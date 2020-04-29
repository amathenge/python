n = 3
address = "221b Baker Street, NW1 6XE, London"  # S. Holmes
employee = {
  'age': 45,
  'role': 'CEO',
  'SSN': 'AB1234567'
}

print(n)
print(address)
print(employee)

f = open('lorem-ipsum.txt','r')
for c in f:
    for x in c:
        print("{}-".format(x), end='')

f.close()
