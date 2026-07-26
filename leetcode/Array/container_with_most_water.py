''' PROBLEM - Container With Most Water
ou are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''


class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        max_vol = 0
        
        while l< r:
            w = r - l
            h = min(height[l], height[r])
            water = w * h

            if water > max_vol:
                max_vol = water
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_vol