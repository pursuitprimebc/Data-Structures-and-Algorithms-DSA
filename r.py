arr = [2,3,4,7,11]
k = 5
for num in arr:
    if num <= k:
        print(num,k)
        k += 1
        
    else:
        break
print(k)