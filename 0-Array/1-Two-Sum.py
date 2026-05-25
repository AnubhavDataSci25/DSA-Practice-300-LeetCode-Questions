"""
LeetCode Question 1: Two Sum

1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
2. You may assume that each input would have exactly one solution, and you may not use the same element twice.
3. You can return the answer in any order.
"""

def twoSum(nums, target):
    hash = {}
    n = len(nums)
    for i in range(0,n):
        remaining = target - nums[i]

        if remaining in hash:
            return [hash[remaining],i]
        else:
            hash[nums[i]] = i

nums = [2,7,11,15]
indices = twoSum(nums, target=9)
print(indices)