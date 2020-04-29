#!/usr/bin/env python

# count the vowels in the file lorem-ipsum.txt

vowels = {}

vowels['a'] = 0
vowels['e'] = 0
vowels['i'] = 0
vowels['o'] = 0
vowels['u'] = 0
vowels['A'] = 0
vowels['E'] = 0
vowels['I'] = 0
vowels['O'] = 0
vowels['U'] = 0

word_b = 0
word_count = 0
word_array = []
word = ''

words_upcase = []

# print("a in dict = {}".format('a' in vowels))

f = open('lorem-ipsum.txt', 'r')

for line in f:
    line = line.strip()
    for c in line:
        if c == ' ':
            word_b = 1
            word_count += 1
            if len(word) > 0:
                word_array.append(word)
                if word[0].upper() == word[0]:
                    words_upcase.append(word)
            word = ''
        else:
            word_b = 0
            word += c
        if c in vowels:
            vowels[c] += 1

# remove punctuation from the list of words
counter = 0
while counter < word_count:
    if word_array[counter][-1] in '.,:;':
        word_array[counter] = word_array[counter][:-1]
    counter += 1

print("word_count is {}".format(word_count))
print("length of word_array is {}".format(len(word_array)))
print("the words are: {}".format(word_array))
print("Upper cased words are {}".format(words_upcase))


for k in vowels:
    print("key {}, value {}".format(k, vowels[k]))
