#Python Classes
#1

class firstexercise:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

obj = firstexercise()
obj.getString()
obj.printString()
        


#2
class Shape:
    def __init__(self):
        pass  

    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        self.length = length  

    def area(self):
        return self.length ** 2  
    
square = Square(5)  
print("Square area:", square.area()) 

shape = Shape()
print("Shape area:", shape.area())  

#3

class Shape:
    def __init__(self):
        pass  

    def area(self):
        return 0  

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  
    
rectangle = Rectangle(5, 4)  
print("Rectangle area:", rectangle.area()) 

shape = Shape()
print("Shape area:", shape.area())  

#4
import math

class Point:
    def __init__(self, x, chickens):
        self.x = x 
        self.chickens = chickens  

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.chickens})")  

    def move(self, dx, dchickens):
        self.x += dx  
        self.chickens += dchickens  
        print(f"Moved to: ({self.x}, {self.chickens})")  

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.chickens - other_point.chickens)**2)
        return distance


point1 = Point(1, 2)
point1.show() 

point2 = Point(4, 6)
point2.show()  

point1.move(2, 3)  

distance = point1.dist(point2)
print("Distance between points:", distance)  


#5
class Bank():
    def __init__(self, account, money):
        self.money = money
        self.account = account

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, money):
        self.money+=money

        return f"You are deposit {money} money"
    
    def withdraw(self, money):
        if self.money - money < 0:
            return "insufficient funds"
        else:
            self.money-=money

            return f"you're balance: {self.money},  and you take {money}"
        
        
bank = Bank("Yeralim", 10000)

print(bank.balance())

print(bank.owner())

print(bank.deposit(10000))

print(bank.withdraw(5000))

print(bank.withdraw(20000))

#6

class Prime:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def filter_prime_numbers(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

n = int(input("n: "))
mylist = []
for i in range(n):
    number = int(input("number: "))
    mylist.append(number)

prime_filter = Prime(mylist)
print(prime_filter.filter_prime_numbers())
























#function_1
#1

def convert(grams):
    ounces = 28.3495231 * grams
    return ounces
grams=int(input("enter the number: "))
print(convert(grams))

#2
def temp(F):
    C = (5 / 9) * (F - 32)
    return C
F=int(input("enter temp: "))
print(temp(F))

#3
def solve(numheads,numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits ==numlegs:
            return rabbits ,chickens
        
    return "Wrong inputs"
numheads = int(input("enter the number of heads: "))
numlegs = int(input("enter the number of legs: "))
print(solve(numheads,numlegs))

#4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers_str = input("enter list numbers: ")
numbers_list = list(map(int, numbers_str.split()))

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)


#5

def permutations(some):
    n = len(some)

    for i in range(n):
        for j in range(n):
            print(some[(j-i)], end=" ")
        print()
k=str(input("string:"))
permutations(k)



#6
def _reverse(strings):
    strings=list(strings.split())
    strings.reverse()
    for i in strings:
        print(i, end=" ")

k=str(input("soz:"))
_reverse(k)

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


has_33([1, 3, 3])
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8

def order007(arr):
    result = []
    for i in arr:
        if i==0 or i==7:
            result.append(i)
    
    flag =  False
    for i in range(len(result)-2):
        if result[i]==result[i+1] and result[i]==0 and result[i+2]==7:
            flag = True
        
    if flag:
        print("True")
    else:
        print("False")

order007([1,2,4,0,0,5,7])
order007([1,0,2,4,0,5,7])
order007([1,7,2,0,4,5,0])

#9

import math
def volumespher(radius):
    V=(4*math.pi*(radius**3))/3
    return V
    
radius=float(input("radius:"))
print(volumespher(radius))

#10

def unique(mylist):
    result = []
    for i in mylist:
        if mylist.count(i) == 1:
            result.append(i)
    return result

n = int(input("n: "))
mylist = []
for i in range(n):
    number = int(input("number: "))
    mylist.append(number)
print(unique(mylist))

#11

def palindrom(text):
    if text==text[::-1]:
        print("YES")
    else:
        print("NO")

text = input("text: ")
palindrom(text)

#12

def histogram(arr):
    for i in arr:
        print("*"*i)
n=input("numbers:")
mylist=list(map(int,n.split()))
histogram(mylist)

#13

from random import randint

def guessanumber():
    print("Hello! What is your name?")
    name = input("name:")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")


guessanumber()

#14

from random import randint

def guessanumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")


guessanumber()
def randomator(start, end, length):
    arr=[randint(start, end)for i in range(length)]
    print(arr)
randomator(1,10,10)



class person:
    def __init__(self):
        self.txt = ""
    def say(self,txt):
        return  f"people said : {self.txt}"





























#function_2
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#1 
def imdb(movies):
    name=input("name:")
    for movie in movies:
        if movie["name"]==name:
            if movie["imdb"]>5.5:
                return True
    return False
print(imdb(movies))

#2
def score(movies):
    result =[]
    for movie in movies:
        if movie["imdb"]>5.5:
            result.append(movie)
    return result
print(score(movies))

#3
name=str(input("name:"))
def category(movies):
    result=[]
    for movie in movies:  
        if movie["category"]==name:
            result.append(movie)
    return result
print(category(movies))
            

#4
def imdvpoint(movies,name):
    sum=0
    cnt=0
    for movie in movies:
        if movie["name"] in name:
            sum+=movie["imdb"]
            cnt+=1
    return sum/cnt
name=[]
while name1!="done":
    
    name1=input("name movie:")
    if name1 == 'done':
        break
    name.append(name1)

print(imdvpoint(movies,name))

#5
def imdvpoint(movies):
    avg=0
    cnt=0
    for movie in movies:
        if movie["category"]==name:
            avg+=movie["imdb"]
            cnt+=1
    return avg/cnt
print(imdvpoint(movies))



import json

def reverse_ex(data):
    reversed_dict = {}  
    for key in reversed(data): 
        reversed_dict[key] = data[key]  
    return reversed_dict  

data = { 
    "Name": "Alice",
    "age": 25,
    "city": "NY"
}

json_str = json.dumps(data, indent=4, ensure_ascii=False)
print(json_str)

#2
parsed_data = json.loads(json_str)

#3
reversed_data = reverse_ex(parsed_data)

#4
print(reversed_data)




if "age" in parsed_data:  
    parsed_data["age"] = 32