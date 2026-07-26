''' PROBLEM - Count Elements With Strictly Smaller and Greater Elements 
Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.
'''

class Solution:
    def countElements(self, nums: list[int]) -> int:
        min_value = min(nums)
        max_value = max(nums)
        
        count = 0
        for i in nums:
            if min_value < i < max_value:
                count += 1
                
        return count