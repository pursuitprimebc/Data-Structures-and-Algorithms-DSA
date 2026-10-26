n = int(input())
x = list(map(int, input().split()))
x.sort()

q = int(input())
for i in range(q):
    m = int(input())
    
    left = 0
    right = n - 1
    affordable_shops = 0
    
    while left <= right:
        mid = (left + right) // 2
        if x[mid] <= m:
            affordable_shops = mid + 1
            left = mid + 1
        else:
            right = mid - 1
            
    print(affordable_shops)