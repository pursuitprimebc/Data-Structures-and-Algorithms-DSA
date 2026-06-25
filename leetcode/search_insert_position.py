''' PROBLEM - Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for i in nums:
            if i==target:
                return count
            elif i>target:
                return count
            count += 1
        return count      