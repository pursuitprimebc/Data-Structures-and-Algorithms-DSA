t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    if sum(a) % 2 == 0:
        print("YES")
    else:
        print("NO")

