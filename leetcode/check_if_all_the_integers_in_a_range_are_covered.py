''' PROBLEM -  1893. Check if All the Integers in a Range Are Covered
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
'''


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        ranges.sort()
        for start, end in ranges:
            if start <= left <= end:
                left = end + 1
            if left > right:
                return True
        return left > right