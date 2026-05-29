"""
LeetCode 268: Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

def missingNum(nums):
    result = len(nums)

    for i in range(len(nums)):
        result += (i - nums[i])
    return result

nums = [3,0,1]
missing_num = missingNum(nums)
print(missing_num)