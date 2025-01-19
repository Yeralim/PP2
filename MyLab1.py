#1
#PYTHON HOME

print ("Hello,world!") 

#2
#PYTHON INTRO

print ("Hello,PP2!")

#3
#PYTHON GET STARTED

import sys
print(sys.version)


#4
#PYTHON SYNTAX

if 5 > 2:
 print("Five is greater than two!") 
       
#5
#PYTHON COMMENTS

#This is a comment

"""
This is a comment
written in
more than just one line
"""

#6
#PYTHON VARIABLES
x = 5
y = "John"
print(x)
print(y) 

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#get the type
x = 5
y = "John"
print(type(x))
print(type(y))


#6.1
#PYTHON VARIABLE-NAMES

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 

#6.2
#Python Variables - Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#6.3
#PYTHON - OUTPUT VARIABLES

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#6.4
#PYTHON - GLOBAL VARIABLES

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#7
#PYTHON DATA TYPES
x = 20.5
print(type(x))

#8
#PYTHON NUMBERS
x = 1
y = 1.1
z = 1j

print(type(x))
print(type(y))
print(type(z)) 


#random
import random
print(random.randrange(1, 10)) #answer: 9

#9
#PYTHON CASTING
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2  

#10
#PYTHON STRINGS
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')  

#string length
a = "Hello, World!"
print(len(a))      

#string array
a = "Hello, World!"
print(a[1])       

#10.1
#PYTHON - SLICING STRINGS

b = "Hello, World!"
print(b[2:5])

#10.2
#PYTHON - MODIFY STRINGS

#replace string
a = "Hello, World!"
print(a.replace("H", "J"))  

#10.3
#PYTHON - STRING CONCATENATION
a = "Hello"
b = "World"
c = a + b 
print(c)  

#10.4
#PYTHON - FORMAT - STRINGS
age = 18
txt = f"My name is Yeralim, I am {age}"
print(txt)      

#10.5
#PYTHON - ESCAPE CHARACTERS
txt = "We are the so-called \"Vikings\" from the north."