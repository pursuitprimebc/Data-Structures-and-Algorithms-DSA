n = int(input())
if n % 4 == 1 or n % 4 == 2:
    print("NO")
else:
    print("YES")
    set1 = []
    set2 = []
   
    if n % 4 == 3:
        set1.extend([1, 2])
        set2.append(3)
        start = 4
    else:
        start = 1
    for i in range(start, n + 1, 4):
        set1.extend([i, i + 3])
        set2.extend([i + 1, i + 2])

    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)