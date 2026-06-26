t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if a[0] == a[1] or a[0] == a[2]:
        common = a[0]
    else:
        common = a[1]

    for i in range(n):
        if a[i] != common:
            print(i + 1)
            break