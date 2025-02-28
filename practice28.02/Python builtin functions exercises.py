#ex1

from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

nums = [2, 3, 4, 5]
result = multiply_list(nums)
print("Product of numbers:", result)


#ex2

def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

text = "Hello World!"
count_case(text)


#ex3

def is_palindrome(s):
    return s == s[::-1]

word = "madam"
print("Is palindrome:", is_palindrome(word))


#ex4

import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")

num = int(input("Enter a number: "))
delay_time = int(input("Enter delay in milliseconds: "))
delayed_sqrt(num, delay_time)


#ex5

def all_true(tup):
    return all(tup)

values = (True, 1, "Hello", 5)
print("All elements are true:", all_true(values))


