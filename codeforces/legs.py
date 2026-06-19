t = int(input())
for i in range(t):
    n = int(input())
    cows = (n//4)
    chicken = ((n%4)//2)
print(cows + chicken)