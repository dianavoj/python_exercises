#Write a program that accepts a sentence and calculate the number of 
#upper case letters and lower case letters.

word = input()

count1 = 0
count2 = 0
for x in word:
    if x.isupper():
        count1 += 1
    if x.islower():
        count2 += 1
print(f'Upper: ', count1)
print(f'Lower: ', count2)