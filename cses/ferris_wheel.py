n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

left = 0
right = n - 1
gondolas = 0

while left <= right:
    if p[left] + p[right] <= x:
        left += 1
    
    right -= 1
    gondolas += 1

print(gondolas)