''' PROBLEM - To Lower Case
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
'''


class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for char in s:
            if 'A' <= char <= 'Z':
                res.append(chr(ord(char) + 32))
            else:
                res.append(char)
        return "".join(res)    

       