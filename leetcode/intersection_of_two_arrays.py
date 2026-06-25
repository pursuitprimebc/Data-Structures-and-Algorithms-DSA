''' PROBLEM -  Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result 
must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = {}
        result = []
        for num in nums1:
            intersection[num] = True

        for num in nums2:
            if intersection.get(num) == True:
                result.append(num)
                intersection[num] = False
        
        return result


