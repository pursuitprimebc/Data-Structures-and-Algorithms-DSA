''' PROBLEM - Shortest Distance to a Character
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
'''

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        res = [0] * n
        
        pos = -float('inf')
        for i in range(n):
            if s[i] == c:
                pos = i
            res[i] = i - pos
            
        pos = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                pos = i
            res[i] = min(res[i], pos - i)
            
        return res