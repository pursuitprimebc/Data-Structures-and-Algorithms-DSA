t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    monsters = []
    for i in range(n):
        rem = a[i] % k
        if rem == 0:
            rem = k
        monsters.append((-rem, i + 1))
    monsters.sort()

    for m in monsters:
        print(m[1], end=" ")
    print()