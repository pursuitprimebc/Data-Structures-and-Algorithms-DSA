''' PROBLEM -Array Partition
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) 
for all i is maximized. Return the maximized sum.
'''
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        maximized_sum = 0
        n = len(nums)
        nums.sort()
        for i in range(0,n,2):
            maximized_sum += nums[i]
        return maximized_sum

# what i code
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        maximized_sum = 0
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        for i in range(0,n,2):
            maximized_sum += nums[i]
        return maximized_sum 
