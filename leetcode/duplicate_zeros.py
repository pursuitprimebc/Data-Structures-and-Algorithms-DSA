''' PROBLEM - 1089. Duplicate Zeros
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
'''

class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                for j in range(n - 1, i, -1):
                    arr[j] = arr[j - 1]
                i += 2
            else:
                i += 1