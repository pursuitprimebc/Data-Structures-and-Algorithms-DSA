''' PROBLEM - Find Pivot Index
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = 0
        leftsum = 0
        pivot_index = -1
        for i in nums:
            total += i
        for i in range(len(nums)):
            current_num = nums[i]
            if leftsum == (total - leftsum - current_num):
                pivot_index = i
                break  
            leftsum += current_num

        return pivot_index    
    