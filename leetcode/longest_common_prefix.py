'''PROBLEM - Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        commonprefix = ""
        for word in zip(*strs):
            if len(set(word)) == 1:
                commonprefix += word[0]
            else:
                break
                
        return commonprefix