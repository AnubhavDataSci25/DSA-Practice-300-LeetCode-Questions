"""
LeetCode 53: Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
# Brute Force Algo
def maxSubarray(nums):
    max_sum = 0
    for st in range(0,len(nums)):
        current_sum = 0
        for end in range(st, len(nums)):
            current_sum += nums[end]
            max_sum = max(max_sum, current_sum)
    return max_sum

# Kadane's Algo
def maxSubarrayKadane(nums):
    max_sum = 0
    current_sum = 0
    for st in range(0,len(nums)):
        current_sum += nums[st] 
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
# max_sum = maxSubarray(nums)
max_sum = maxSubarrayKadane(nums)
print(f"Max Subarray sum: {max_sum}")