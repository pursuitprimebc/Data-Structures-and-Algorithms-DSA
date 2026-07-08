t = int(input())
for i in range(t):
    s = input()
    pair = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            pair = True
            break
            
    if pair:
        print(1)
    else:
        print(len(s))