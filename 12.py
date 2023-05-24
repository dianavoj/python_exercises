#Write a program, which will find all such numbers between 1000 and 3000 
#(both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on 
#a single line.
result=[]
for i in range(1000,3001):
    a, b, c, d = str(i)
    if all (int(x) % 2 == 0 for x in [a,b,c,d]):
        result.append(str(i))
print(','.join(result))   
    
