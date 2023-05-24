#Write a program that computes the value of a+aa+aaa+aaaa 
#with a given digit as the value of a.

x = input()

x1 = int(str(x) + str(x))
x2 = int(str(x) + str(x) + str(x)) 
x3 = int(str(x) + str(x) + str(x)+ str(x))
x = int(x)
print(x+x1+x2+x3)
