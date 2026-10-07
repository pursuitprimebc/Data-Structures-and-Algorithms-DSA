t = int(input().strip())
    
for i in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
        
    max_blank = 0
    current_blank = 0
    for num in a:
        if num == 0:
            current_blank += 1
            if current_blank > max_blank:
                max_blank = current_blank
        else:
                current_blank = 0
                
    print(max_blank)