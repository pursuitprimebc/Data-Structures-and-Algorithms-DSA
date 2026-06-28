t = int(input())
for i in range(t):
    n,a,b,c = map(int, input().split())
    days = 0
    count = 0
    dist_in_3days = a + b + c
            
    full_cycles = n // dist_in_3days
    rem_dist = n % dist_in_3days

    days = full_cycles * 3

    if rem_dist > 0:
        if rem_dist <= a:
            days += 1
        elif rem_dist <= a + b:
            days += 2
        else:
            days += 3

    print(days)