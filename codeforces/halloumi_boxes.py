t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k >= 2:
        print("YES")
    else:
        if a == sorted(a):
            print("YES")
        else:
            print("NO")
