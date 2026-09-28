''' PROBLEM - Repetitions
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. 
This is a maximum-length substring containing only one type of character.

Input
The only input line contains a string of n characters.

Output
Print one integer: the length of the longest repetition.

Constraints
1 <= n <= 10^6
'''


s = input()
curr_len = 1
max_len = 1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        curr_len += 1
    else:
        if curr_len > max_len:
            max_len = curr_len
        curr_len = 1
if curr_len > max_len: 
    max_len = curr_len
print(max_len)


    


