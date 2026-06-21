'''PROBLEM - Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it .
'''

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        
        for j in range(1, rowIndex): 
            row[j] = row[j - 1] * (rowIndex - j + 1) // j
            
        return row