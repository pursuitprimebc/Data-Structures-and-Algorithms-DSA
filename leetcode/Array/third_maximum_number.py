''' PROBLEM -414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
    
        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

        if third != float('-inf'):
            return third
        else:
            return first