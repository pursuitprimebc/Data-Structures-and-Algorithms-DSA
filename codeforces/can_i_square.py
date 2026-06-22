t =int(input())
for i in range(t):
    total = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        total += a[i]
    
    low = 1
    high = 10**9  
    perfect_square = False
    
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        
        if square == total:
            perfect_square = True
            break
        elif square < total:
            low = mid + 1  
        else:
            high = mid - 1 

    if perfect_square:
        print("YES")
    else:
        print("NO")