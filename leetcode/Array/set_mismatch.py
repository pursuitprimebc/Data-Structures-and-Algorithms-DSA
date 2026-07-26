''' PROBLEM - 5. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        original = set()
        duplicate = 0
        for i in nums:
            if i in original:
                duplicate = i
            original.add(i)
        
        expected_sum = n*(n+1)//2
        current_sum = sum(original)
        missing_num = expected_sum - current_sum
        return [duplicate,missing_num]



