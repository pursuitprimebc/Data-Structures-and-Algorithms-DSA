t = int(input())
for i in range(t):
    n,m,k = map(int,input().split())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    ways = 0
    for coin_b in b:
        for coin_c in c:
            if coin_b + coin_c <= k:
                ways += 1

    print(ways)



