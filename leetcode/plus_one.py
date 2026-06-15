''' PROBLEM - Plus One
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        New_string = ""
        for digit in digits:
            New_string = New_string + str(digit)
        New_int = int(New_string) + 1
        Final_List = []
        for i in range(len(str(New_int))):
            Final_List.append(int(str(New_int)[i]))
        return Final_List