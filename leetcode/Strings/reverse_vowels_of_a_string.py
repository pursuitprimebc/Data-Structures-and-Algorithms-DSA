''' problem -  Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        vowels_in_s = []
        for i in s:
            if i in vowels_set:
                vowels_in_s.append(i)
        
        result = []
        for j in s:
            if j in vowels_set:
                reversed_vowel = vowels_in_s.pop()
                result.append(reversed_vowel)
            else:
                result.append(j)
                
        res = ""
        for a in result:
            res += a
            
        return res