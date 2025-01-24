#LAB 2
#1
#BOOLEANS

print(10 > 9)
print(10 == 9)
print(10 < 9) 

  
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#2
#PYTHON OPERATIONS

print(100 + 5 * 3)

#3
#PYTHON LISTS

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) 


#3.1
#Python - Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#3.2
#Python - Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#3.3
#Python - Add List Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#3.3
#Python - Remove List Items

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#3.4
#Python - Loop Lists

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
#3.5
#Python - List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#3.6
#Python - Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#3.7
#Python - Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


#3.8
#Python - Join Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#4
#Python Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#4.1
#Python - Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#4.2
#Python - Update Tuples

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#4.3
#Python - Unpack Tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


#4.4
#Python - Loop Tuples

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  

#4.5
#Python - Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#5
#Python Sets

thisset = {"apple", "banana", "cherry"}
print(thisset)

#5.1
#Python - Access Set Items

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#5.2
#Python - Add Set Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#5.3
#Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#5.4
#Python - Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#5.5
#Python - Join Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#6
#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#6.1
#Python - Access Dictionary Items

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)

#6.2
#Python - Change Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#6.3
#Python - Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#6.4
#Python - Remove Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#6.5
#Python - Loop Dictionaries

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)


#6.6
#Python - Copy Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#6.7
#Python Dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#7
#Python If ... Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#8
#Python While Loops

i = 1
while i < 6:
  print(i)
  i += 1

#9
#Python For Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)