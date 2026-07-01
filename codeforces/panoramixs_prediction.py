def isprime(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
n,m = map(int,input().split())
 
next_prime = n + 1
while not isprime(next_prime):
    next_prime += 1
if next_prime == m:
    print('YES')
else:
    print('NO')


