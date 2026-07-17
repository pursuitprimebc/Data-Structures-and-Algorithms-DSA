t = int(input())
for j in range(t):
    n ,k = map(int, input().split())
    min_package = n
    for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i <= k:
                    min_package = min(min_package, n // i)
                if n // i <= k:
                    min_package = min(min_package, i)
    print(min_package)