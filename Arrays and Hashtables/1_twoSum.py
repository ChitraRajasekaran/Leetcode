class Solution(object):
    def twoSum(self, nums, target):
        m = {}  # Step 1: Initialize the hash table
        for i, x in enumerate(nums):  # Step 2: Enumerate through nums
            y = target - x  # Step 3: Calculate complement y
            if y in m:  # Step 4: Check if y is present in the hash table
                return [m[y], i]  # Return the indices of the two elements adding up to target
            m[x] = i  # Step 5: Store x with its index in hash table for future reference
        
s_instance = Solution()
test1 = s_instance.twoSum([10, 15, 3, 7],17)
print(test1)


































