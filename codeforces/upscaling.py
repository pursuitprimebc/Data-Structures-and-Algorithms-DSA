t = int(input())

for i in range(t):
    n = int(input())

    r1 = ("##.." * n)[:2 * n]
    r2 = ("..##" * n)[:2 * n]

    for i in range(2 * n):
        if (i // 2) % 2 == 0:
            print(r1)
        else:
            print(r2)