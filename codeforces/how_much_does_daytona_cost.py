t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    res = False
    for i in range(n):
        if k == a[i]:
            res = True
    if res:
        print('YES')
    else:
        print('NO')        


