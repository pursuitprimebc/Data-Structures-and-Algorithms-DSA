word = input()
if len(word) == 1 or word[1:].isupper():
    result = ""
    for char in word:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
            
    print(result)
else:
    print(word)