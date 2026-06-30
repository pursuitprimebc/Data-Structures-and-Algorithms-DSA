t = int(input())
for i in range(t):
    a,b = input().split( )
    w1 = b[:1] + a[1:]
    w2 = a[:1] + b[1:]
    print(w1,w2)
