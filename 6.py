
#q = Square root of [(2 * c * d)/h]
#c = 50
#h = 30
#d = input

import math

#the solution below isn't working because there will be comma printed at the end
d = input('enter  number: ').split(',')

for i in d:
    i = int(i)
    c = str(int(math.sqrt((2 * 50 * i) / 30)))
    
    print (c, end=',')
    #how to print without the comma at the end??

#####
# different solution:
d = input('enter  number: ').split(',')

result = []
for i in d:
    i = int(i)
    c = str(int(math.sqrt((2 * 50 * i) / 30)))
    result.append(c)

print(','.join(result))