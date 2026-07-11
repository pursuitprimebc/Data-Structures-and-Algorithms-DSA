'''PROBLEM - 832. Flipping an Image
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
'''


class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            
            while left <= right:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                
                left += 1
                right -= 1
                
        return image