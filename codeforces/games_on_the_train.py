t = int(input())
for i in range(t):
    n = int(input())
    h = list(map(int,input().split()))
    min_h = 10000000
    max_h = 0
    for i in range(n):
        if h[i] > max_h:
            max_h = h[i]

        if h[i] < min_h:
            min_h = h[i]        

    print(max_h - min_h + 1)
