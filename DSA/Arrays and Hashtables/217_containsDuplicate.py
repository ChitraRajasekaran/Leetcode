nums = [1,1,1,3,3,4,3,2,4,2]

counter = 1

has = {}

def containsDuplicate(nums):
    for i in nums:
        if i in has: 
            return True
        else: 
            has[i] = counter
    return False




print(containsDuplicate(nums))
