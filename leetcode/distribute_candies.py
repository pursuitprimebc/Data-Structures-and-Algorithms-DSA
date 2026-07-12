''' PROBLEM - 575. Distribute Candies
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number 
of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
'''


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        total_candies = 0
        for i in candyType:
            total_candies += 1
            
        doctor_limit = total_candies // 2
        unique_candies = 0
        d = {}
        for j in candyType:
            if j not in d:
                d[j] = True
                unique_candies += 1
        if unique_candies < doctor_limit:
            return unique_candies
        else:
            return doctor_limit