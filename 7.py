#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

x, y = input('Enter two numbers: ').split(',')
x = int(x)
y = int(y)
#print (x, y)

my_list = []
master_list = []
for i in range (0, x):
    new_list = []
    for j in range (0,y):
        result = i*j
        new_list.append(result)
        my_list.append(result)
    master_list.append(new_list)

    
        
print(master_list)

