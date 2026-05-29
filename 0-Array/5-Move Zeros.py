"""
Leetcode 283: Move Zeros

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

def moveZeros(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        
    return nums

nums = [0,0,1]
nums_lst = moveZeros(nums)
print(nums_lst)