a, b, n = map(int, input().split())

turn = 0

while True:
    fixed = a if turn == 0 else b
    
    x = fixed
    y = n
    while y > 0:
        x, y = y, x % y
    take = x
    
    if n < take:
        print(1 - turn)
        break
        
    n -= take
    turn = 1 - turn

