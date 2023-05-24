#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
#Suppose the following input is supplied to the program:
#hello world and practice makes perfect and hello world again
#Then, the output should be:
#again and hello makes perfect practice world
from collections import Counter
#input
string = input().split(' ')
#count number of words

word_count = Counter(string)
word_dict = dict(word_count)

print(word_dict)
new_list = []
for key in word_dict:
    value = word_dict[key]
    #print(value)
    if value < 2:
        new_list.append(key)
print(' '.join(sorted(new_list)))

#####
word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))