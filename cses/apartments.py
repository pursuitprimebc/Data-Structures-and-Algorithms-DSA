n, m, k = map(int, input().split())
applicants = sorted(map(int, input().split()))
apartments = sorted(map(int, input().split()))

i = 0 
j = 0 
matches = 0

while i < n and j < m:
    if apartments[j] < applicants[i] - k:
        j += 1
    elif apartments[j] > applicants[i] + k:
        i += 1
    else:
        matches += 1
        i += 1
        j += 1

print(matches)