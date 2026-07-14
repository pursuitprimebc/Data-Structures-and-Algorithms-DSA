n = int(input())
home_uniform = []
guest_uniform = []
    
for i in range(n):
    h, a = map(int,input().split())
    home_uniform.append(int(h))
    guest_uniform.append(int(a))

same_uniform = 0
for i in range(n):
    for j in range(n):
        if home_uniform[i] == guest_uniform[j]:
            same_uniform += 1
print(same_uniform)

