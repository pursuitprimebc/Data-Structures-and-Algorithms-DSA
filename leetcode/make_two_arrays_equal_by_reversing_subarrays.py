''' PROBLEM - 1460. Make Two Arrays Equal by Reversing Subarrays
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
'''


class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        counts = {}
        for n in target:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
                
        for n in arr:
            if n in counts:
                counts[n] -= 1
            else:
                return False 
                
        for count in counts.values():
            if count != 0:
                return False

        return True