''' PROBLEM - Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
'''



class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            alphanum = ord(i) - ord('A') + 1
            res = (res*26 ) + alphanum
        return res 