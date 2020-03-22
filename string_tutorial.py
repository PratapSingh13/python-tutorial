#Python Strings
#All string methods returns new values they do not change original String
#String Literals-In python string literals are surrounded by either single quotation marks or double quotation marks
# 'hello' is same as "hello"
# You can display a string literal with the print()

print("Hello")
print('Hello')

# Assign String to a Variable
myString = "Hello"
print(myString)

# Multiline Strings
# Python allows us to assign a multiline string to a variable by using three quotes
myString = """My name is Yogendra Pratap Singh,
I worked at OpsTree Solutions"""
print(myString)

# or three single quotes
myString = '''My name is Yogendra Pratap Singh,
I worked at OpsTree Solutions'''
print(myString)

# Strings are Arrays
#Like many other programming languages, strings in python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Get the character at position 1 (remember the first character has the position 0)
myString = "Yogendra Pratap Singh"
print(myString[9])              # returns-:P

#Slicing
#You can return a range of character by using the slice syntax. Specify the start index and the end index seperated by a colon, to return a part of the string
#Get the characters from the position 2 to 5(not included)
myString = "Yogendra Pratap Singh"
print(myString[2:5])            # returns-:gen

myString = "Pratap Singh"
print(myString[-5:-1])          # output-:Sing

#String Length
#To get the length of String use len()
myString = "Yogendra Pratap Singh"
print(len(myString))            # returns-:21

#String Method
#Python has a set of built-in methods that you can use on Strings

#The strip() method removes any whitespace from the beginning or the end
myString = " Yogendra Pratap Singh "
print(myString.strip())             # returns-:"Yogendra Pratap Singh"

#The lower() method returns the string in lower case
myString = "Yogendra Pratap Singh"
print(myString.lower())             # returns-:"yogendra pratap singh"

#The upper() method returns the string in upper case
myString = "Yogendra Pratap Singh"
print(myString.upper())             # returns-:"YOGENDRA PRATAP SINGH"

#The replace() method replaces a string with another string
myString = "Yogendra Pratap Singh"
print(myString.replace("Y", "y"))   # returns-;yogendra Pratap Singh

#The split() method splits the string into sub-strings if it finds instances of the separator
myString = "Yoogendra Pratap Singh"
print(myString.split(" "))          # returns-:['Yoogendra', 'Pratap', 'Singh']

#The capitalize() method converts the first character to upper case of the String
myString = "yogendra pratap singh"
print(myString.capitalize())        # returns-:Yogendra pratap singh

#The count() method returns the number of times a specified value occurs in a string
myString = "Yogendra Pratap Singh"
print(myString.count("a"))

#The find() method searches the string for a specified value and returns the position of where it was found
#In case of not found it will return -1 as output
myString = "Yogendra Pratap Singh"
print(myString.find("S"))

#The index() method searches the string for a specified value and returns the position of where it was found
myString = "Yogendra Pratap Singh"
print(myString.index("Singh"))