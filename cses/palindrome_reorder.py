from collections import Counter
s = input().strip()
def solve():
    counts = Counter(s)

    odd_chars = [char for char, count in counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        print("NO SOLUTION")
        return

    first_half =[]
    mid = ''
    for char in sorted(counts.keys()):
        count = counts[char]
        first_half.append(char * (count//2))
        if count%2 != 0:
            mid = char
    first_half = "".join(first_half)

    print(first_half + mid + first_half[::-1])

if __name__ == '__main__':
    solve()