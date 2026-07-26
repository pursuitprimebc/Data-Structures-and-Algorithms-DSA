''' PROVLEM - 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        a = {}
        flag = False
        for i in nums:
            if i in a:
                return True
            a[i]=0
        return False

# i could have this solution also but i avoid using pythonic fuctions.

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
