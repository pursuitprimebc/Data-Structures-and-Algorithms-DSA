t = int(input())
for i in range(t):
    n = input()
    c = 0
    for i in n:
        c+=1
    if c>10:
        print(f"{n[0]}{c-2}{n[c-1]}")
    else:
        print(n)
            