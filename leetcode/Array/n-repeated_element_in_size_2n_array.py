'''PROBLEM - 961. N-Repeated Element in Size 2N Array
You are given an integer array nums with the following properties:
nums.length == 2 * n.
nums contains n + 1 unique values, n of which occur exactly once in the array.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
'''


class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        s = set()
     
        for num in nums:
            if num in s:
                return num
            s.add(num)
