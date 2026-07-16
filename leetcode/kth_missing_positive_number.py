''' PROBLEM - 1539. Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.
'''


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            else:
                break
        return k