#ex1

size_list=input("size list:")
my_list=list(map(int,size_list.split()))
multiplay=1
for i in my_list:
    multiplay*=i
print(multiplay)


#ex2

def count_letters(letter):
    upper=0
    lower=0
    for i in letter:
        if i>="A" and i<="Z":
            upper+=1
        else:
            lower+=1
    print("sum upper case:", upper)
    print("sum lower case:", lower)
            
        

soilem=str(input("enter sentence:"))
count_letters(soilem)


#ex3

def polindrom(soilem,teris_soilem):
    for i in soilem:
        for j in teris_soilem:
            if i!=j:
                return False
                break
            return True
        
    

sentence=str(input("enter sentence:"))
soilem_reverse=''.join(reversed(sentence))
print(polindrom(sentence,soilem_reverse))


#ex4

import math
import time

time_miliseconds=int(input("Enter  miliseconds:"))
time2_miliseconds=int(input("Enter 2nd miliseconds:"))

print(f"Square root of {time_miliseconds} after {time2_miliseconds} miliseconds is {math.sqrt(time_miliseconds)}")


#ex5

size_mylist=input("Enter  mylist:")
mylist=list(map(int,size_mylist.split()))
print("all True mylist:",all(mylist))


