#Variables are containers for storing data values
#Unlike other Programming languages, Python has no command for declaring a variable.

var1 = 5
var2 = "Yogendra"
print(var1)
print(var2)

var3 = 4             #var3 is of type int
var3 = "Pratap"      #var3 is now changed and type of str
print(var3)

#String variables can be declared either by using single or double quotes
#myname = "Yogendra"
#myname = 'Yogendra'

#Assign Value to Multiple Variables

#Python allows us to assign values to multiple variable in one line
x, y, z = "Yogendra", "Pratap", "Singh"
print(x)
print(y)
print(z)

#Python also allows us to assign same value to multiple variables in one line
x = y = z = "Yogendra"
print(x)
print(y)
print(z)

#Output Variables
#Python print statement is often used to output variables

#To combine both text and variable, Python uses the + character
myvar = "Yogendra"
print("My name is " + myvar)

#We can also use the + character to add a variable to another variable
myvar1 = "Yogendra"
myvar2 = "Pratap"
myvar3 = "Singh"
myvar = myvar1 + myvar2 + myvar3
print(myvar)

#For numbers the + character works as a mathematical operator
num1 = 5
num2 = 10
print(num1 + num2)

#It will not work if you try to combine string and a number



#Global Variables

#Varibles that are created outside of a function
#Global variable can be used by everyone both inside of function and outside

#Create a variable outside of a function, and use it inside the function
name = "Yogendra"

def myfunc():
    print("My name is " + name)
myfunc()    


#Create a vaariable inside a function, with the same name as the global variable
name = "Yogendra"

def myfunc():
    name = "Pratap"
    print("My name is " + name)  # My name is Pratap
myfunc()

print("My name is " + name)      # My name is Yogendra


#Use of global keyword
"""
Normally when we create a variable inside a function that variable is local and can only be used inside that function
To create a global variable inside a function we can use the global keyword
"""

def myfunc():
    global name
    name = "Yogendra"
myfunc()

print("My name is " + name)

#To change the value of a global variable inside a function refer to the variable by using the global keyword
name = "Yogendra"

def myfunc():
    global name
    name = "Pratap"
myfunc()

print("My name is " + name)