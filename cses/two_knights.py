n = int(input())

for k in range(1, n + 1):
    total_pairs = (k**2 * (k**2 - 1)) // 2
    attack_pairs = 4 * (k - 1) * (k - 2)
    print(total_pairs - attack_pairs)

