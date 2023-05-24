#Write a program that accepts a sentence and calculate the number of 
#letters and digits.
x = input()
count1 = 0
new_string = x.replace(' ', '')

for y in new_string:
    if y.isalpha():
        count1 += 1

count2 = 0
for y in x:
    if y.isdigit():
        count2 += 1
print(f'Numbers ', count2)
print(f'Letters', count1)

