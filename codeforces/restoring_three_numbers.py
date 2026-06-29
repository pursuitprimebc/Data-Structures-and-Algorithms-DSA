integers = list(map(int, input().split()))
integers.sort()
n = integers[3]
a = n - integers[0]
b = n - integers[1]
c = n - integers[2]
print(a,b,c)

