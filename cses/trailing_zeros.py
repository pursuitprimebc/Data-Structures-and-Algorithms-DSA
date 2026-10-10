n = int(input().strip())
zeros = 0
while n >= 5:
    n //= 5
    zeros += n
        
print(zeros)