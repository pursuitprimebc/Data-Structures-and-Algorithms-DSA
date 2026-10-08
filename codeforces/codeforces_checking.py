t = int(input().strip())
target = set("codeforces") 
for i in range(t):
    c = input().strip()
    if c in target:
        print("YES")
    else:
        print("NO")