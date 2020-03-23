# Python If...Else

#If condition
myVar1 = 33
myVar2 = 66
if (myVar2 > myVar1):
    print("myVar2 is greater than myVar1")

#Indentation-Python relies on indentation(whitespace at the beginning of a line) to define scope in the code. Other languages uses curly-brackets for this purpose.
myVar1 = 33
myVar2 = 66
if (myVar1 < myVar2):
print("myVar2 is greater than myVar1")        #will return IndentationError

#Elif
myVar1 = 33
myVar2 = 66
if (myVar1 < myVar2):
    print("myVar2 is greater than myVar1")
elif myVar1 == myVar2:
    print("Both are equal")

#Else
myVar1 = 100
myVar2 = 33
if myVar1 < myVar2:
    print("myVar2 is greater than myVar1")
elif myVar1 == myVar2:
    print("Both are equal")
else:
    print("myVar1 is greater than myVar2")


