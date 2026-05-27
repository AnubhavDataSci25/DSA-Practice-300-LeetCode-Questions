"""
LeetCode 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

def containsDuplicate(nums):
    hash={}
    count=0
    for i in nums:
        if i not in hash:
            hash[i] = count + 1
        else:
            return True
    return False

nums = []
print(containsDuplicate(nums))