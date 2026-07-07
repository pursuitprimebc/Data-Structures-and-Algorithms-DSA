t = int(input())
for i in range(t):
    x1,x2,x3 = map(int,input().split())
    a = max(x1,x2,x3)
    b = min(x1,x2,x3)
    res = a-b
    print(res)
