#write a program to generate a dictionary {i, i*i} that includes numbers between 1 and n(input), both included
n = int(input('Enter a number: '))

dict = {}
for i in range(1, n+1):
    dict[i] =  i * i
print(dict)

