t = int(input())

for i in range(t):
    n = int(input())

    row1 = ("##.." * n)[:2 * n]
    row2 = ("..##" * n)[:2 * n]

    for i in range(2 * n):
        if (i // 2) % 2 == 0:
            print(row1)
        else:
            print(row2)