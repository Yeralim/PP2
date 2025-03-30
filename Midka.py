def squares(nums):
    for i in nums:
        if i%2 == 0:
            yield list(map(lambda x: x ** 2, nums))
            
            
nums = [1, 2, 3, 4, 5, 6]  
doubled = squares(nums)
print(doubled)

map[key]

list[]