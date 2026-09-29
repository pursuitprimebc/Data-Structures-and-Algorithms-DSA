import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    if n == 2 or n == 3:
        sys.stdout.write("NO SOLUTION\n")
        return

    odds = [str(i) for i in range(n if n % 2 != 0 else n - 1, 0, -2)]
    
    evens = [str(i) for i in range(n if n % 2 == 0 else n - 1, 1, -2)]

    sys.stdout.write(" ".join(odds + evens) + "\n")



if __name__ == '__main__':
    solve()
