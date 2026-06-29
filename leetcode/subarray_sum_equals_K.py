''' PROBLEM -  Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sums = {0: 1}
        current_sum = 0
        total_subarrays = 0
        for num in nums:
            current_sum += num
            target = current_sum - k
            if target in prefix_sums:
                total_subarrays += prefix_sums[target]
                
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
        return(total_subarrays) 