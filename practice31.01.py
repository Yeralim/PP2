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
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

#2
def highly_rated_movies(movies):
    return [movie for movie in movies if is_highly_rated(movie)]

#3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

#4
def average_imdb_score(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

#5
def average_score_by_category(movies, category):
    filtered_movies = movies_by_category(movies, category)
    return average_imdb_score(filtered_movies)

#examples
print(is_highly_rated(movies[0]))
print(highly_rated_movies(movies))
print(movies_by_category(movies, "Romance"))
print(average_imdb_score(movies))
print(average_score_by_category(movies, "Romance"))
