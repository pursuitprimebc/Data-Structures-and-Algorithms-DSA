''' PROBLEM - Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''



class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = []
        
        for i in words:
            reversed_word = i[::-1]
            reversed_words.append(reversed_word)
        result = " ".join(reversed_words)
        return result

    