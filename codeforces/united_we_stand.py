t = int(input().strip())
for i  in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort()

    if a[0] == a[-1]:
        print("-1")
    else:
        b = []
        c = []

        max_val = a[-1]
        for num in a:
            if num == max_val:
                c.append(num)
            else:
                b.append(num)

        print(len(b),len(c))
        print(*(b))
        print(*(c))
