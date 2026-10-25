t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()

    freq = {}
    for char in s:
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1

    odd_count = 0
    for count in freq.values(): 
        if count % 2 != 0:
            odd_count = odd_count + 1

    if odd_count <= k + 1:
        print("YES")
    else:
        print("NO")