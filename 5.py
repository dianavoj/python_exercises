#Define a class which has at least two methods:

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

#creates a class with 3 methods: __init__, getstring, printstring
class Object():
    def __init__ (self):
        self.s = ''

#prompts the user for input and stores it in s
    def getstring(self):
        self.s = input()

#converts input s to upper case

    def printstring(self):
        print(self.s.upper())

#creating an object
x = Object()
#running the two methods on the object
x.getstring()
x.printstring()