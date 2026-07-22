t = int(input())
for i in range(t):
    n = int(input())
    s = str(n)
    if len(s) >= 3 and s.startswith("10") and s[2] != '0' and int(s[2:]) >= 2:
        print("YES")
    else:
        print("NO")


