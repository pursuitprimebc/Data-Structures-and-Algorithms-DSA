t = int(input())
for i in range(t):
    n = input()
    summands = []
    count = 0
    d = len(n)
    for i in range(d):
        if n[i] != '0':
            summands.append(n[i] + ((d-(1+i))* '0'))
    print(len(summands))
    print(*summands)