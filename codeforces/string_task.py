s = input().strip().lower()
vowel = ['a','e','i','o','u','y','A','E','I','O','U','Y']
new_word = ""
for i in s:
    if i not in vowel:
        new_word += i 
result = '.' + '.'.join(new_word)
print(result) 