''' PROBLEM - Detect Pattern of Length M Repeated K or More Times
Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.

A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.

Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
'''


class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        consecutive_matches = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                consecutive_matches += 1
                if consecutive_matches == (k - 1) * m:
                    return True
            else:
                consecutive_matches = 0
                
        return False