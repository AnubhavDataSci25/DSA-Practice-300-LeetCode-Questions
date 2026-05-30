"""
LeetCode 349: Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""

def intersectionOfTwoArr(nums1, nums2):
    hashset=set(nums1)
    result=[]

    for i in nums2:
        if i in hashset:
            result.append(i)
            hashset.remove(i)
    return result

nums1=[2,5,9]
nums2=[2,6,5,5,8,2,9,9]
result = intersectionOfTwoArr(nums1, nums2)
print(result)