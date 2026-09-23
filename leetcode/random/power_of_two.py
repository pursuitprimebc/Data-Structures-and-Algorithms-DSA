''' PROBLEM - 231. Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            
        while n % 2 == 0:
            n //= 2
            
        return n == 1

# got to know about Bitwise AND 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be strictly greater than 0
        # n & (n - 1) clears the lowest set bit
        return n > 0 and (n & (n - 1)) == 0