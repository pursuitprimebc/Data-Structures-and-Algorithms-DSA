t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    low = 1
    high = 2000000000
    
    while low <= high:
        mid = (low + high) // 2
        water = 0
        for h in a:
            if mid > h:
                water += (mid - h)
                
        if water <= x:
            low = mid + 1
        else:
            high = mid - 1
            
    print(high)