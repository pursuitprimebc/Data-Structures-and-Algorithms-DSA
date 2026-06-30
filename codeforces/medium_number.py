t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    
    if (a > b and a < c) or (a < b and a > c):
        medium = a
    elif (b > a and b < c) or (b < a and b > c):
        medium = b
    else:
        medium = c
        
    print(medium)