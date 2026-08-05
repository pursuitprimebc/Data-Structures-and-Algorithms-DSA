''' PROBLEM - Longer Contiguous Segments of Ones than Zeros
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.
'''


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones, max_zeros = 0, 0
        curr_ones, curr_zeros = 0, 0
        
        for char in s:
            if char == '1':
                curr_ones += 1
                curr_zeros = 0  
                max_ones = max(max_ones, curr_ones)
            else:
                curr_zeros += 1
                curr_ones = 0  
                max_zeros = max(max_zeros, curr_zeros)
                
        return max_ones > max_zeros