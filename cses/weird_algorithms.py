n = int(input())
m = n
res = []
while m >1:
    if m%2==0:
        m = m//2
    else:
        m *= 3
        m += 1
    res.append(m)
print(n,*res)