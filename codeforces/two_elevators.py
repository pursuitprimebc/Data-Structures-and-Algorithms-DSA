t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    res =''
    t1 = abs(a - 1)
    t2 = abs(b - c) + abs(c - 1)
    if t1 < t2:
        res = "1"
    elif t2 < t1:
        res= "2"
    else:
        res= "3"
    print(res)



