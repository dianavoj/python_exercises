import math 

list_of_numbers = input()
list_of_int = list_of_numbers.split(',')

result = []
for i in list_of_int:
    x = int(i)
    if x % 2 != 0:
        y = x**2
        result.append(str(y))
    else:
        continue       
print(','.join(result))